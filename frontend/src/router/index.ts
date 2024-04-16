import { createRouter, createWebHistory } from 'vue-router'
import Homepage from "@/pages/homepage/Homepage.vue";
import Login from "@/pages/admin/Login.vue";
import Admin from "@/pages/admin/Admin.vue";
import Profile from "@/pages/admin/Profile.vue";
import CreateDocument from "@/pages/admin/CreateDocument.vue";
import EditDocument from "@/pages/admin/EditDocument.vue";
import Documents from "@/pages/admin/Documents.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/:notFound",
      component: Homepage,
    },
    {
      path: '/',
      name: 'home',
      component: Homepage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      children: [
        {
          path: '',
          component: Profile
        },
        {
          path: 'documents',
          component: Documents
        },
        {
          path: 'documents/create',
          component: CreateDocument
        },
        {
          path: 'documents/edit/:id',
          component: EditDocument
        }
      ]
    }
  ]
})

export default router
