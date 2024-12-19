<template>
  <div class="registration-container">
  <form class="registration-form" @submit.prevent="createAuth">
    <h1 class="registration-title">Авторизация</h1>
    <my-input
      v-model="auth.username"
      type="text"
      placeholder="Логин"
      class="form-input"
    />
    <my-input
      v-model="auth.password"
      type="password"
      placeholder="Пароль"
      class="form-input"
    />
    <button class="form-button" type="submit">Войти</button>
  </form>
</div>

</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      auth: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async createAuth() {
      if (!this.auth.username || !this.auth.password) {
        alert("Все поля обязательны для заполнения!");
        return;
      }

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/login",
          {
            username: this.auth.username,
            password: this.auth.password,
          },
          {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            withCredentials: true,
          }
        );

        alert("Вы успешно вошли в систему!");
        this.auth.username = "";
        this.auth.password = "";
        await this.getRole();
      } catch (error) {
        alert("Ошибка авторизации. Проверьте данные и попробуйте снова.");
      }
    },

    async getRole() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/auth/get_role",
          {
            withCredentials: true,
          }
        );
        alert(`Ваша роль: ${response.data.role}`);
      } catch (error) {
        alert("Ошибка получения роли. Попробуйте снова.");
      }
    },
  },
};
</script>

<style scoped>
.registration-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 400px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.registration-title {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
  font-family: "Arial", sans-serif;
}

.registration-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-button {
  padding: 10px;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-button:hover {
  background-color: #0056b3;
}


</style>
