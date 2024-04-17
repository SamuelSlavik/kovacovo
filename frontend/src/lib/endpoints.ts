export class Endpoints {
  private static readonly baseUrl = "https://kovacovo-backend.vercel.app/api";

  // USER / ADMIN --------------------------------------------------------
  static get login(): string {
    return `${Endpoints.baseUrl}/user/login`;
  }
  static get logout(): string {
    return `${Endpoints.baseUrl}/user/logout`;
  }
  static updateUser(id: string): string {
    return `${Endpoints.baseUrl}/user/update/${id}`;
  }
  static retrieveUser(id: string): string {
    return `${Endpoints.baseUrl}/user/retrieve/${id}`;
  }
  static get retrieveCurrentUser(): string {
    return `${Endpoints.baseUrl}/user/`;
  }
  static get updateUserEmail(): string {
    return `${Endpoints.baseUrl}/user/update/email`;
  }
  static get updateUserPassword(): string {
    return `${Endpoints.baseUrl}/user/update/password`;
  }


  // DOCUMENTS ------------------------------------------------------------
  static get getDocuments(): string {
    return `${Endpoints.baseUrl}/documents`;
  }
  static getDocument(id: string): string {
    return `${Endpoints.baseUrl}/documents/${id}`;
  }
  static createDocument(): string {
    return `${Endpoints.baseUrl}/documents/create`;
  }
  static updateDocument(id: string): string {
    return `${Endpoints.baseUrl}/documents/update/${id}`;
  }
  static deleteDocument(id: string): string {
    return `${Endpoints.baseUrl}/documents/delete/${id}`;
  }
}