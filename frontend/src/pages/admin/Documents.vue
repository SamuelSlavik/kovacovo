<script setup lang="ts">
import Heading from "@/components/Heading.vue";
import {useRouter} from "vue-router";
import {inject, onMounted, ref} from "vue";
import type {Document} from "@/lib/models";
import {documentsApi} from "@/lib/apiHelpers";
import Loader from "@/components/Loader.vue";

const router = useRouter()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const documents = ref<Document[]>([])

const loadDocuments =  async() => {
  try {
    loading.value = true
    const response: any = await documentsApi.getDocuments()
    documents.value = response.data

  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get documents: " + error.message})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadDocuments()
  console.log(documents)
})

const deleteDocument = async (id: string) => {
  if (!window.confirm("Are you sure you want to delete this document?")) {
    return;
  }

  try {
    loading.value = true
    const response: any = await documentsApi.deleteDocument(id)
    if (response.status === 200) {
      notificationStore.addNotification({type: "success", message: "Document deleted successfully"})
      await loadDocuments()
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to delete document: " + error.message})
  } finally {
    loading.value = false
  }
}

</script>

<template>
<div>
  <button @click="() => {router.push('/admin/documents/create')}" class="button">Add new document</button>
  <Loader v-if="loading"/>
  <div v-else>
    <div v-for="document in documents" key="document.id" class="documents-table">
      <div class="documents-table__name"><router-link :to="'/admin/documents/edit/' + document.id">{{document.title}}</router-link></div>
      <!--<div><a download target="_blank" :href="'http://localhost:8000/' + document.document">{{document.document}}</a></div>-->
      <div class="documents-table__year">{{document.year}}</div>
      <div class="documents-table__toolbar">
        <router-link :to="'/admin/documents/edit/' + document.id">EDIT</router-link>
        <a @click="() => deleteDocument(document.id)">DELETE</a>
      </div>
    </div>
  </div>
</div>
</template>

<style>
.documents-table {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.documents-table__name {
  flex: 3;
}

.documents-table__year {
  flex: 1;
  text-align: center;
}

.documents-table__toolbar {
  flex: 1;
  display: flex;
  justify-content: right;
  gap: 1rem;

  a:first-child {
    color: green;
  }
  a:nth-child(2) {
    color: red;
  }
}
</style>