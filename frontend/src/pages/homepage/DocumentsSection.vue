<script setup lang="ts">
import {useRouter} from "vue-router";
import {computed, inject, onMounted, ref} from "vue";
import type {Document} from "@/lib/models";
import {documentsApi} from "@/lib/apiHelpers";

const router = useRouter()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const documents = ref<Document[]>([])
const groupedDocuments = ref<{ [key: number]: Document[] }>({});

const loadDocuments =  async() => {
  try {
    loading.value = true
    const response: any = await documentsApi.getDocuments()
    documents.value = response.data
    groupDocumentsByYear();

  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get documents: " + error.message})
  } finally {
    loading.value = false
  }
}

const groupDocumentsByYear = () => {
  groupedDocuments.value = documents.value.reduce((acc: any, doc: any) => {
    if (!acc[doc.year]) {
      acc[doc.year] = [];
    }
    acc[doc.year].push(doc);
    return acc;
  }, {});
};

const sortedYears = computed(() => {
  return Object.keys(groupedDocuments.value).sort((a, b) => Number(b) - Number(a));
});

onMounted(() => {
  loadDocuments()
  console.log(documents)
})
</script>

<template>
  <section>
    <Heading>Zverejnené dokumenty</Heading>
    <Loader v-if="loading"/>
    <div v-else class="documents">
      <div v-for="year in sortedYears" :key="year">
        <h2>{{ year }}</h2>
        <div>
          <div
              v-for="(document, index) in groupedDocuments[parseInt(year)]"
              :key="document.id"
              :class="{ 'document-entry': true, 'border-bottom': index !== groupedDocuments[parseInt(year)].length - 1 }"
          >
            <p>
              {{ document.title }}<br/>
              <a download target="_blank" :href="'http://localhost:8000/' + document.document">Stiahnuť súbor</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style>
.documents {
  display: flex;
  flex-direction: column;
  gap: 3rem;
}
.document-entry {
  margin-bottom: 10px; /* Adjust as needed */
}

.border-bottom {
  border-bottom: 1px solid #ccc; /* Define your border style */
}

</style>