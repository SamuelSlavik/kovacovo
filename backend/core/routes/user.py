from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..db.databases import get_session
from ..schemas.user import CreateUser, Token
from ..db.models import User
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_route = APIRouter()


# Function to hash a password
def get_hashed_password(password: str) -> str:
    hashed_password = bcrypt_context.hash(password)
    return hashed_password


# Function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, session):
    user = session.query(User).filter(User.email == username).first()
    if not user:
        return
    if not verify_password(password, user.password):
        return
    return user


def create_access_token(email: str, id: int):
    encode = {"sub": email, "id": id}
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: int = payload.get("id")
        if email is None or id is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        user = User(id=id, email=email)
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@user_route.post("/signup")
async def register(user: CreateUser, session: Session = Depends(get_session)):
    # Search database with email, if it returns any user, raise exception
    existing_user = session.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = get_hashed_password(user.password)

    new_user = User(email=user.email, password=hashed_password)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "user created successfully"}


@user_route.post("/login", response_model=Token)
async def login_for_access_token(credentials: CreateUser, session: Session = Depends(get_session)):
    print("aasdfqwefasdfqwefasdf")
    user = authenticate_user(credentials.email, credentials.password, session)
    print("bqwefasdfqewfadsfqewfsdf")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user.email, user.id)

    return {"access_token": token, "token_type": "bearer"}


@user_route.get("/")
async def get_user(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"id": user.id, "email": user.email}
