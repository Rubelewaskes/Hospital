<template>
    <form @submit.prevent="updateDoctor">
      <h4>Изменение доктора</h4>
  
      <my-selectPlace :optionsPlace="optionsPlace" />
      <my-input
        v-model="doctor.first_name"
        type="text"
        placeholder="Имя"
      />
      <my-input
        v-model="doctor.second_name"
        type="text"
        placeholder="Фамилия"
      />
      <my-input
        v-model="doctor.third_name"
        type="text"
        placeholder="Отчество"
      />
      <my-input
        v-model="doctor.phone_number"
        type="text"
        placeholder="Телефон"
      />
      <my-input
        v-model="doctor.experience"
        type="text"
        placeholder="Опыт"
      />
      <my-input
        v-model="doctor.areas_list"
        type="text"
        placeholder="Участки(через запятую)"
      />
      <my-button
        class="btn"
        style="align-self: flex-end; margin-top: 15px"
        type="submit"
      >
        Сохранить изменения
      </my-button>
    </form>
  </template>
  
  <script>
  import MySelect from "@/Components/UI/MySelect";
  import axios from "axios";
  
  export default {
    components: {
      MySelect,
    },
    props: {
      initialDoctor: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        doctor: {
            first_name: "",
            second_name: "",
            third_name: "",
            phone_number: "",
            experience: "",
        areas_list: [],
      },
    };
    },
    methods: {
        
      async updateDoctor() {
        try {
          const response = await axios.put(
            `http://127.0.0.1:8000/check_up/update/${this.doctor.id}`,
            this.doctor,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          );
          alert("Изменения успешно сохранены!");
          console.log("Ответ сервера:", response.data);
        } catch (error) {
          console.error("Ошибка обновления:", error);
          if (error.response) {
            console.error("Ответ сервера:", error.response.data);
          }
          alert("Произошла ошибка. Попробуйте снова.");
        }
      },
    },
    mounted() {
      this.fetchOptionsPlace(); // Загружаем данные при монтировании
    },
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    justify-content: baseline; 
  }
  </style>
  