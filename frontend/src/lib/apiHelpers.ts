import type {Credentials, NewDocument, Token, User} from "@/lib/models";
// @ts-ignore
import axios from "axios";
// @ts-ignore
import type {AxiosResponse} from "axios";
import {Endpoints} from "@/lib/endpoints";

const getHeaders = () => {
  return { headers: { "Authorization": "Bearer " + localStorage.getItem("token") }}
}

export class userApi {
  static async login(credentials: Credentials) : Promise<AxiosResponse<Token, Token>>  {
    return await axios.post(
      Endpoints.login,
      credentials,
      getHeaders()
    )
  }
  static async retrieveCurrentUser() : Promise<AxiosResponse<User, User>> {
    return await axios.get(
      Endpoints.retrieveCurrentUser,
      getHeaders()

    )
  }
  static async updateEmail(email: string) : Promise<AxiosResponse<User, User>> {
    return await axios.put(
      Endpoints.updateUserEmail,
      {new_email: email},
      getHeaders()
    )
  }
}


export class documentsApi {
  static async getDocuments(): Promise<AxiosResponse<Document[], any>> {
    return await axios.get(
      Endpoints.getDocuments,
      getHeaders()
    )
  }
  static async getDocument(id: string): Promise<AxiosResponse<Document, any>> {
    return await axios.get(
      Endpoints.getDocument(id),
      getHeaders()
    )
  }
  static async createDocument(formData: FormData): Promise<AxiosResponse<any>> {
    return axios.post(
      Endpoints.createDocument(), // Updated to use the correct URL for document creation
      formData,
      {
        headers: {
          "Authorization": "Bearer " + localStorage.getItem("token"),
          'Content-Type': 'multipart/form-data',
        }
      }
    );
  }
  static async updateDocument(id: string, formData: FormData): Promise<AxiosResponse<Document, any>> {
    return await axios.put(
      Endpoints.updateDocument(id),
      formData,
      {
        headers: {
          "Authorization": "Bearer " + localStorage.getItem("token"),
          'Content-Type': 'multipart/form-data',
        }
      }
    );
  }
  static async deleteDocument(id: string): Promise<AxiosResponse<Document, any>> {
    return await axios.delete(
      Endpoints.deleteDocument(id),
      getHeaders()
    )
  }
}
