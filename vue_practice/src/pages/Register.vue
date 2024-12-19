<template>
    <div class="registration-container">
      <h1 class="registration-title">Регистрация</h1>
      <form @submit.prevent="register" class="registration-form">
        <label for="email" class="form-label">Email</label>
        <input
          id="email"
          v-model="formData.email"
          type="email"
          placeholder="Введите email"
          class="form-input"
          required
        />
  
        <label for="password" class="form-label">Пароль</label>
        <input
          id="password"
          v-model="formData.password"
          type="password"
          placeholder="Введите пароль"
          class="form-input"
          required
        />
  
        <button type="submit" class="form-button">Зарегистрироваться</button>
      </form>
      <p class="error-message" v-if="error">{{ error }}</p>
      <p class="success-message" v-if="success">{{ success }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        formData: {
          email: "",
          password: "",
          isDoctor: false,
        },
        error: null,
        success: null,
      };
    },
    methods: {
      async register() {
        this.error = null;
        this.success = null;
        try {
          const response = await axios.post("http://127.0.0.1:8000/register", {
            email: this.formData.email,
            password: this.formData.password,
            is_doctor: this.formData.isDoctor,
            is_active: true,
            is_superuser: false,
            is_verified: false,
          },
          {
            withCredentials: true, 
          }
        );
          if (response.status === 201) {
            this.success = "Регистрация прошла успешно!";
          }
        } catch (err) {
          this.error = err.response?.data?.detail || "Ошибка при регистрации.";
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
  width: 100%; /* Для совпадения размеров */
  margin: 0 auto;
  padding: 30px; /* Увеличить до совпадения */
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  min-height: 400px; /* Добавлено для фиксации высоты */
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
  
  .form-label {
    font-size: 1rem;
    color: #555;
    text-align: left;
  }
  
  .form-input {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .form-checkbox {
    margin-top: 5px;
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
  
  .error-message {
    color: #ff4d4d;
    font-size: 1rem;
    margin-top: 10px;
  }
  
  .success-message {
    color: #4caf50;
    font-size: 1rem;
    margin-top: 10px;
  }
  </style>
  