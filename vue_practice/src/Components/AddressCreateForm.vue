<template lang="html">
    <div v-if="isFormVisible">
      <form @submit.prevent="createAddress">
        <h4>Добавление диагноза</h4>
  
        <my-input v-model="address.id" type="text" placeholder="ID:" />
        <my-input
          v-model="address.street"
          type="text"
          placeholder="Улица:"
        />
        <my-input
          v-model="address.house"
          type="text"
          placeholder="Дом:"
        />
        <my-input
          v-model="address.building"
          type="text"
          placeholder="Здание:"
        />
        <my-input
          v-model="address.flat"
          type="text"
          placeholder="Квартира:"
        />
        <my-input
          v-model="address.area_id"
          type="text"
          placeholder="Участок:"
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
      initialAddress: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        address: {
          id: "",
          name: "",
        },
        isFormVisible: true, // Флаг для отображения формы
      };
    },
    methods: {
      async createAddress() {
        try {
          // Отправка данных на сервер
          const response = await axios.post(
            "http://127.0.0.1:8000/address/add_new",
            this.address,
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
  
          this.$emit("create", this.address); // Передаём данные родителю
          this.$emit("update:show", false);
  
          alert("Адрес успешно добавлен!");
        } catch (error) {
          console.error("Ошибка создания адрес:", error);
          if (error.response && error.response.data) {
            console.error("Детали ошибки:", error.response.data);
          }
          alert(
            "Ошибка при добавлении адреса. Проверьте данные и попробуйте снова."
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
  