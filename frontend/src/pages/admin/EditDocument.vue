<script setup lang="ts">
import type { NewDocument } from "@/lib/models";
import {inject, onMounted, ref} from "vue";
import Heading from "@/components/Heading.vue";
import {documentsApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const notificationStore: any = inject('notificationStore')
const loading = ref<boolean>(false)
const router = useRouter()

const document_id = router.currentRoute.value.params.id[0] || ""

const document_path = ref<string>("")

const newDocument = ref<NewDocument>({
  title: "",
  year: null,
  document: null
})

const loadDocument = async () => {
  try {
    loading.value = true
    const response: any = await documentsApi.getDocument(document_id)
    newDocument.value.title = response.data.title
    newDocument.value.year = response.data.year
    document_path.value = response.data.document
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get document: " + error.message})
  } finally {
    loading.value = false
  }
}

const editDocument = async () => {
  const formData = new FormData();
  formData.append("title", newDocument.value.title);
  // @ts-ignore
  formData.append("year", newDocument.value.year); // Ensure year is a string
  if (newDocument.value.document) {
    formData.append("document", newDocument.value.document);
  }

  try {
    const response = await documentsApi.updateDocument(document_id, formData);
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

onMounted(() => {
  loadDocument()
})
</script>

<template>
  <form @submit.prevent="editDocument">
    <label>Title</label>
    <input
        type="text"
        name="title"
        v-model="newDocument.title"
        placeholder="Title"
        required
    />
    <label>
      Year
    </label>
    <input
        type="number"
        name="year"
        v-model="newDocument.year"
        placeholder="Year"
        required
    />
    <p>
      File:<br/>
      <a download target="_blank" :href="'http://localhost:8000/' + document_path">{{document_path}}</a>
    </p>

    <br/>
    <label>Upload new file if you wanna change it</labeL>
    <input
        type="file"
        name="document"
        accept="application/pdf"
        @change="onFileChange($event)"
    />

    <br/>
    <button class="button">Update Document</button>
  </form>
</template>

<style>

</style>