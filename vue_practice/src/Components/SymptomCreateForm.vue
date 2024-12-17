<template lang="html">
    <div v-if="isFormVisible">
      <form @submit.prevent="createSymptom">
        <h4>Добавление симптома</h4>
  
        <my-input v-model="symptom.id" type="text" placeholder="ID:" />
        <my-input
          v-model="symptom.name"
          type="text"
          placeholder="Наименование:"
        />
  
        <my-button
          class="btn"
          style="align-self: flex-end; margin-top: 15px"
          type="submit"
        >
          Сохранить изменения
        </my-button>
      </form>
    </div>
  </template>
  
  <script>
  import MySelect from "@/Components/UI/MySelect";
  import axios from "axios";
  
  export default {
    components: {
      MySelect,
    },
    props: {
      initialSymptom: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        symptom: {
          id: "",
          name: "",
        },
        isFormVisible: true, // Флаг для отображения формы
      };
    },
    methods: {
      async createSymptom() {
        try {
          // Отправка данных на сервер
          const response = await axios.post(
            "http://127.0.0.1:8000/symptom/add_new",
            this.symptom,
            {
              withCredentials: true,
  
              headers: {
                "Content-Type": "application/json",
              },
            }
          );
          console.log(response.status);
          if (response.status === 200) {
            window.location.reload(); // Перезагрузка страницы
          }
  
          this.$emit("create", this.symptom); // Передаём данные родителю
          this.$emit("update:show", false);
  
          alert("Симптом успешно добавлен!");
        } catch (error) {
          console.error("Ошибка создания симптома:", error);
          if (error.response && error.response.data) {
            console.error("Детали ошибки:", error.response.data);
          }
          alert(
            "Ошибка при добавлении симптома. Проверьте данные и попробуйте снова."
          );
        }
      },
    },
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    justify-content: baseline;
  }
  div:empty {
    display: none;
  }
  </style>
  