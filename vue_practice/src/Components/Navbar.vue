<template>
  <div class="navbar">
    <div @click="$router.push('/')">Главная</div>
    <div class="navbar__btns">
      <my-button @click="$router.push('/patients')">Пациенты</my-button>
      <my-button class="exit_btn" @click="logout">Выход из акка</my-button>
      <my-button @click="$router.push('/profile')">Профиль(-)</my-button>
    </div>
    <!-- Модальное окно -->
    <div v-if="isLogoutModalVisible" class="modal-overlay" @click="closeModal">
      <div class="modal" @click.stop>
        <p>Вы успешно вышли из аккаунта.</p>
        <my-button @click="closeModal">Закрыть</my-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      isLogoutModalVisible: false, // Управляет видимостью модального окна
    };
  },
  methods: {
    async logout() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/logout", null, {
          headers: {
            Accept: "application/json",
          },
          withCredentials: true,
        });

        if (response.status === 204) {
          console.log("Вы успешно вышли из аккаунта");
          this.isLogoutModalVisible = true; // Показать модальное окно
          this.$router.push("/"); // Перенаправление на главную страницу
        } else {
          console.error("Ошибка при выходе из аккаунта:", response);
        }
      } catch (error) {
        console.error("Ошибка запроса при выходе из аккаунта:", error);
      }
    },
    closeModal() {
      this.isLogoutModalVisible = false; // Закрыть модальное окно
    },
  },
};
</script>

<style scoped>
.navbar {
  height: 50px;
  background-color: lightgrey;
  box-shadow: 2px 2px 4px grey;
  display: flex;
  align-items: center;
  padding: 0 15px;
  margin-bottom: 15px;
}
.navbar__btns {
  margin-left: auto;
}
.exit_btn {
  margin: 0px 10px;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}
</style>
