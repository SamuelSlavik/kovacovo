<script setup lang="ts">
import {RouterLink, RouterView, useRouter} from 'vue-router'
import {useUserStore} from "@/stores/user-store";
import {inject, onMounted, ref} from "vue";
import type {User} from "@/lib/models";
import axios from "axios";
import {Endpoints} from "@/lib/endpoints";

const loading = ref<boolean>(false)
const user = useUserStore()
const notificationStore: any = inject('notificationStore')

const checkUser = async () => {
  try {
    loading.value = true

    const response = await axios.get<User>(
        Endpoints.retrieveCurrentUser,
        {headers: {Authorization: `Bearer ${localStorage.getItem("token") || ""}`}}
    )
    if (response.status === 200) {
      user.setUserData(response.data)
    }
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  checkUser()
})
</script>

<template>
  <header>
    <h1><router-link to="/">Pozemkové Združenie <br/> Kováčovo </router-link></h1>
    <router-link style="margin-top: 2rem; display: block" v-if="user.email" to="/admin">Admin</router-link>
  </header>

  <RouterView />

  <footer>

  </footer>

  <Notifications />
</template>

<style>
:root {
  --green: #609966;
  --light-green: #9DC08B;
  --primary: rgb(85, 85, 85);
  --secondary: rgba(85, 85, 85, 0.8);
  --tertiary: rgba(85, 85, 85, 0.2);
  --background: #EDF1D6;
  --secondary-background: #40513B;
  --breakpoint: 1200px;
  --editable: rgba(0, 153, 153, 1);
}
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  transition: all 0.5s ease;
  scroll-behavior: smooth;
}
body {
  min-height: 100vh;
  color: var(--primary);
  background-color: var(--background);
  font-family: "Open Sans", sans-serif;
  scroll-behavior: smooth;
  line-height: 2rem;
}
a {
  text-decoration: none;
  color: var(--green);
}

h2, h3 {
  color: var(--green);
}

header {
  text-align: center;
  background-color: var(--secondary-background);
  color: var(--background) !important;
  padding: 8rem 2rem;
}
header h1 a {
  color: var(--background);
  font-size: 2rem;
  font-weight: bold;
  text-transform: uppercase;
  text-shadow: 0 0 0.5rem var(--green);
}
</style>
