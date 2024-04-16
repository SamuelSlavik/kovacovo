import { createApp } from 'vue'
import { createPinia } from 'pinia'
//@ts-ignore
import axios from "axios";


import App from './App.vue'
import router from './router'
import Container from "@/components/Container.vue";
import Heading from "@/components/Heading.vue";
import Loader from "@/components/Loader.vue";

// @ts-ignore
import Notifications from "notification-quark"
import "notification-quark/dist/style.css"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Notifications)


app.component("Container", Container)
app.component("Heading", Heading)
app.component("Loader", Loader)

app.mount('#app')

axios.interceptors.response.use(
  (response: any) => response,
  async (error: any) => {
    // If the response status is 401 (Unauthorized), navigate to the login page
    if (error.response.status === 401) {
      await router.push('/login');
    }
    return Promise.reject(error);
  }
);

