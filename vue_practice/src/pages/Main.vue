<template>
  <div class="container">
    <h1 class="welcome_h1">Добро пожаловать</h1>
    <div class="links">
      <router-link to="/authorization" class="link">Авторизация</router-link>
      <router-link to="/register" class="link">Регистрация</router-link>
      <router-link to="/patients" class="link">Пациенты</router-link>
      <router-link to="/patientsAdmin" class="link">Пациенты (админ)</router-link> 
      <router-link to="/doctors" class="link">Врачи</router-link>
      <router-link to="/diagnosis" class="link">Диагнозы</router-link>
      <router-link to="/symptoms" class="link">Симптомы</router-link>
      <router-link to="/areas" class="link">Участки</router-link>
      <router-link to="/addresses" class="link">Адреса</router-link>
    </div>
  </div>
</template>

<script>
import { RouterLink } from "vue-router";

export default {};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.welcome_h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
  font-family: 'Arial', sans-serif;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.link {
  display: inline-block;
  padding: 10px 15px;
  font-size: 1.2rem;
  color: #fff;
  background-color: #007bff;
  border-radius: 5px;
  text-decoration: none;
  font-family: 'Arial', sans-serif;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.link:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

.link:active {
  background-color: #003f7f;
}
</style>
