<template>
  <form @submit.prevent="createRegister">
    <my-input v-model="register.username" type="text" placeholder="Логин" />
    <my-input v-model="register.password" type="password" placeholder="Пароль" />
    <my-button class="btn" type="submit">Войти</my-button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      register: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async createRegister() {
      if (!this.register.username || !this.register.password) {
        alert("Все поля обязательны для заполнения!");
        return;
      }

      try {
        console.log("Отправляемые данные:", this.register);

        const response = await axios.post(
          "http://127.0.0.1:8000/login",
          {
            username: this.register.username,
            password: this.register.password,
          },
          {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            withCredentials: true,
          }
        );

        console.log("POST-запрос успешен:", response);

        alert("Вы успешно вошли в систему!");
        this.register.username = "";
        this.register.password = "";

        console.log("Вызов getRole");
        await this.getRole(); // Вызов GET-запроса
      } catch (error) {
        console.error("Ошибка авторизации:", error);
        alert("Ошибка авторизации. Проверьте данные и попробуйте снова.");
      }
    },

 
  },
  mounted() {
    this.getRole();
  },
};
</script>
