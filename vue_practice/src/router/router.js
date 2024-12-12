import Authorization from "@/pages/Authorization.vue";
import Main from "@/pages/Main.vue";
import PatientIdPage from "@/pages/PatientIdPage.vue";
import PatientPage from "@/pages/PatientPage.vue";
import Register from "@/pages/Register.vue";
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
    path: "/patients/:id",
    component: PatientIdPage,
  },
  {
    path: "/authorization",
    component: Authorization,
  },
  {
    path: "/register",
    component: Register,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

export default router;
