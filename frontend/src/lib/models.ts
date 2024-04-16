export type User = {
  id: string;
  email: string;
}
export type Credentials = {
  email: string;
  password: string;
}
export type Token = {
  access_token: string;
  token_type: string;
}


export type Document = {
  id: string
  title: string
  year: number
  document: string
}
export type NewDocument = {
  title: string
  year: number | null
  document: File | null
}



