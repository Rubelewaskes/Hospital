import AdminAllDoctors from "@/pages/AdminAllDoctors.vue";
import Authorization from "@/pages/Authorization.vue";
import DiagnosisAll from "@/pages/DiagnosisAll.vue";
import Main from "@/pages/Main.vue";
import PatientIdPage from "@/pages/PatientIdPage.vue";
import PatientPage from "@/pages/PatientPage.vue";
import Register from "@/pages/Register.vue";
import AdminAllSymptoms from "@/pages/AdminAllSymptoms.vue";
import AdminAllAreas from "@/pages/AdminAllAreas.vue";
import { createRouter, createWebHistory } from "vue-router";
import AdminAllAddresses from "@/pages/AdminAllAddresses.vue";
import PatientPageAdmin from "@/pages/PatientPageAdmin.vue";

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
    path: "/patientsAdmin",
    component: PatientPageAdmin,
  },

  {
    path: "/patients/:patient_id",
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
  {
    path: "/doctors",
    component: AdminAllDoctors,
  },
  {
    path: "/diagnosis",
    component: DiagnosisAll,
  },
  {
    path: "/symptoms",
    component: AdminAllSymptoms,
  },
  {
    path: "/areas",
    component: AdminAllAreas,
  },
  {
    path: "/addresses",
    component: AdminAllAddresses,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

export default router;
