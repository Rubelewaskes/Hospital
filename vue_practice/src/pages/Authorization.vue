<template>
  <form @submit.prevent="createAuth">
    <my-input v-model="auth.username" type="text" placeholder="Логин" />
    <my-input v-model="auth.password" type="password" placeholder="Пароль" />
    <my-button class="btn" type="submit">Войти</my-button>
  </form>
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
        console.log("Отправляемые данные:", this.auth);

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
      } catch (error) {
        console.error("Ошибка авторизации:", error);
        alert("Ошибка авторизации. Проверьте данные и попробуйте снова.");
      }
    },

    async getRole() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/get_role", {
          withCredentials: true,
        });

        console.log("Ответ сервера:", response.data);
        alert(`Ваша роль: ${response.data.role}`);
      } catch (error) {
        console.error("Ошибка при получении роли:", error);
        alert("Ошибка получения роли. Попробуйте снова.");
      }
    },
  },
  mounted() {
    this.getRole();
  },
};
</script>
