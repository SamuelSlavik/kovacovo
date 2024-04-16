import {defineStore} from "pinia";
import type {User} from "@/lib/models";

export const useUserStore: any = defineStore(
  "user", {
    state: () : any => ({
      id: '',
      email: '',
    }),
    actions: {
      setUserData(user: User): void {
        this.id = user.id;
        this.email = user.email;
      },
      logOut (): void {
        this.id = '';
        this.email = '';
      }
    },
  }
)