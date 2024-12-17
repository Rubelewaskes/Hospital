<template>
    <form @submit.prevent="updateDiagnosis">
      <h4>Изменение диагноза</h4>
  
      <my-selectPlace :optionsPlace="optionsPlace" />
      <my-input
        v-model="diagnosis.id"
        type="text"
        placeholder="ID"
      />
      <my-input
        v-model="diagnosis.name"
        type="text"
        placeholder="Наименование"
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
      initialDiagnosis: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        diagnosis: {
            id: "",
            name: "",
      },
    };
    },
    methods: {
        
      async updateDiagnosis() {
        try {
          const response = await axios.put(
            `http://127.0.0.1:8000/diagnosis/update_one/${this.diagnosis.id}`,
            this.diagnosis,
            {
              
            withCredentials: true,
          
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
  