<template>
  <div class="auth-container">
    <form class="auth-form" @submit.prevent="createAuth">
      <h1 class="auth-title">Авторизация</h1>
      <my-input v-model="auth.username" type="text" placeholder="Логин" class="auth-input" />
      <my-input v-model="auth.password" type="password" placeholder="Пароль" class="auth-input" />
      <my-button class="auth-btn" type="submit">Войти</my-button>
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
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f7f9fc;
  padding: 20px;
}

.auth-form {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 30px;
  width: 100%;
  max-width: 400px;
  text-align: center;
  display: flex;
  flex-direction: column;
}

.auth-title {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.auth-input,
.auth-btn {
  width: 100%; 
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box; 
}

.auth-btn {
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.auth-btn:hover {
  background-color: #0056b3;
}

.auth-btn:active {
  background-color: #003f7f;
}

</style>
