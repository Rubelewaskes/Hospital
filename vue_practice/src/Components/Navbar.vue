<template>
  <div class="navbar">
    <div @click="$router.push('/')">Главная</div>
    <div class="navbar__btns">
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
  height: 60px;
  background-color: #007bff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  padding: 0 20px;
  border-radius: 0 0 10px 10px;
  color: #fff;
  font-family: 'Arial', sans-serif;
  margin-bottom: 10px;
}

.navbar div {
  font-size: 1.2rem;
  cursor: pointer;
  transition: color 0.3s ease, transform 0.2s ease;
}

.navbar div:hover {
  color: #f9f9f9;
  transform: scale(1.05);
}

.navbar__btns {
  margin-left: auto;
  display: flex;
  gap: 10px;
}

.exit_btn {
  background-color: #dc3545;
  color: #fff;
  font-weight: bold;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.exit_btn:hover {
  background-color: #a71d2a;
  transform: scale(1.05);
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
  background: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 80%;
  max-width: 400px;
}

.modal p {
  margin-bottom: 15px;
  font-size: 1.2rem;
  color: #333;
}

.modal my-button {
  background-color: #007bff;
  color: #fff;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.modal my-button:hover {
  background-color: #0056b3;
}
</style>

