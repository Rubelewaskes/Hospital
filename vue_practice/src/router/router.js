import ChekupPage from "@/pages/ChekupPage.vue";
import Main from "@/pages/Main.vue";
import PatientIdPage from "@/pages/PatientIdPage.vue";
import PatientPage from "@/pages/PatientPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/patients",
    component: PatientPage,
  },
  {
    path: "/checkup",
    component: ChekupPage,
  },
  {
    path: "/patients/:id",
    component: PatientIdPage,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

export default router;
