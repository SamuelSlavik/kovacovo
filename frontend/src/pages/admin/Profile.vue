<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import {inject, onMounted, ref} from "vue";
import {userApi} from "@/lib/apiHelpers";
import Heading from "@/components/Heading.vue";

const router = useRouter()
const notificationStore: any = inject('notificationStore')
const user = useUserStore()
const loading = ref<boolean>(false)

const newEmail = ref<string>("")
const newPassword = ref<string>("")
const newPasswordRepeated = ref<string>("")

const logout = () => {
  try {
    user.logOut()
    localStorage.setItem("token", "")
    router.push('/')
    notificationStore.addNotification({type: "success", message: "Logged out successfully"})
  } catch (error) {
    notificationStore.addNotification({type: "error", message: "Could not log out"})
  }
}

const updateEmail = async () => {
  try {
    loading.value = true
    const response: any = await userApi.updateEmail(newEmail.value)
    if (response.status === 200) {
      user.setUserData(response.data)
      notificationStore.addNotification({type: "success", message: "Email updated successfully"})
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to update email: " + error.message})
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <Loader v-if="loading"/>
  <div class="section-logout">
    <Heading>{{user.email}}</Heading>
    <br/>
    <button @click="logout" class="button">Log Out</button>
    <br/>
    <br/>
    <br/>
    <Heading>Edit documents</Heading>
    <br/>
    <button @click="() => {router.push('/admin/documents')}" class="button">Edit Documents</button>
  </div>
  </template>

<style>
.section-logout {
  * {
    margin: auto;
  }
}
</style>