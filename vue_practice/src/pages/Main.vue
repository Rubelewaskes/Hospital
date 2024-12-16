<template>
  <div>
    <h1 class="welcome_h1">Добро пожаловать</h1>
    <router-link to="/patients" class="patients_h1">Пациенты</router-link>
    <router-link to="/authorization" class="patients_h1"
      >Авторизация</router-link
    >
    <router-link to="/doctors">Врачи</router-link>
  </div>
</template>
<script>
import { RouterLink } from "vue-router";

export default {};
</script>
<style scoped>
.welcome_h1 {
  margin: 0px 15px;
}
.patients_h1 {
  margin: 0px 15px;
}
</style>
