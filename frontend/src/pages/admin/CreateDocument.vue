<script setup lang="ts">
import type { NewDocument } from "@/lib/models";
import {inject, ref} from "vue";
import Heading from "@/components/Heading.vue";
import {documentsApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const notificationStore: any = inject('notificationStore')
const loading = ref<boolean>(false)
const router = useRouter()

const newDocument = ref<NewDocument>({
  title: "",
  year: null,
  document: null
})

const submitDocument = async () => {
  if (!newDocument.value.document) {
    notificationStore.addNotification({ type: "error", message: "Please select a document file" });
    return;
  }

  const formData = new FormData();
  formData.append("title", newDocument.value.title);
  formData.append("year", newDocument.value.year); // Ensure year is a string
  formData.append("document", newDocument.value.document); // Append the file

  try {
    const response = await documentsApi.createDocument(formData);
    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Document created successfully" });
      await router.push('/admin/documents');
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to create document: ${response.data.message}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to create document: ${error.message}` });
  }
};

const onFileChange = (event: any) => {
  newDocument.value.document = event.target.files[0]
  console.log(newDocument.value.document)
}
</script>

<template>
  <form @submit.prevent="submitDocument">
    <input
      type="text"
      name="title"
      v-model="newDocument.title"
      placeholder="Title"
      required
    />
    <input
      type="number"
      name="category"
      v-model="newDocument.year"
      placeholder="Year"
      required
    />
    <input
        type="file"
        name="document"
        accept="application/pdf"
        @change="onFileChange($event)"
        required
    />

    <br/>
    <button class="button">Submit new Document</button>
  </form>
</template>

<style>

</style>