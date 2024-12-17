<template lang="html">
    <div v-if="isFormVisible">
      <form @submit.prevent="createArea">
        <h4>Добавление участка</h4>
  
        <my-input v-model="area.id" type="text" placeholder="ID:" />
  
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
      initialArea: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        area: {
          id: "",
        },
        isFormVisible: true, // Флаг для отображения формы
      };
    },
    methods: {
      async createArea() {
        try {
          // Отправка данных на сервер
          const response = await axios.post(
            "http://127.0.0.1:8000/area/add_new",
            this.area,
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
  
          this.$emit("create", this.area); // Передаём данные родителю
          this.$emit("update:show", false);
  
          alert("Участок успешно добавлен!");
        } catch (error) {
          console.error("Ошибка создания участка:", error);
          if (error.response && error.response.data) {
            console.error("Детали ошибки:", error.response.data);
          }
          alert(
            "Ошибка при добавлении участка. Проверьте данные и попробуйте снова."
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
  