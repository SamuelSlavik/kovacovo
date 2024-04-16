<script setup lang="ts">

import {inject, onMounted, ref} from "vue";
import {userApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const loading = ref<boolean>(false)
const router = useRouter()
const notificationStore: any = inject('notificationStore')

onMounted(async () => {
  try {
    loading.value = true
    const response: any = await userApi.retrieveCurrentUser()
    if (response.status != 200) {
      await router.push('/login')
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get user: " + error.message})
  } finally {
    loading.value = false
  }
})

</script>

<template>
  <Container :global="true">
    <Loading v-if="loading"/>

    <RouterView v-else />
  </Container>
</template>

<style>
</style>