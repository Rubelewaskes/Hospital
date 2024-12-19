<template>
    <div>
      <h1>Профиль пользователя</h1>
      <div v-if="user">
        <p><strong>Email:</strong> {{ user.email }}</p>
      </div>
      <div v-else>
        <p>Загрузка данных...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "UserProfile",
    data() {
      return {
        user: null, 
      };
    },
    methods: {
      async fetchUserProfile() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/auth/get_me", {
            headers: {
              Accept: "application/json",
            },
            withCredentials: true,
          });
          this.user = response.data; 
        } catch (error) {
          console.error("Ошибка при получении профиля:", error);
        }
      },
    },
    mounted() {
      this.fetchUserProfile(); 
    },
  };
  </script>
  
  <style scoped>
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  p {
    font-size: 18px;
  }
  </style>
  