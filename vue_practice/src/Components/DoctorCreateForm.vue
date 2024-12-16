<template lang="html">
  <div v-if="isFormVisible">
    <form @submit.prevent="createDoctor">
      <h4>Добавление доктора</h4>

      <my-input v-model="doctor.first_name" type="text" placeholder="Имя" />
      <my-input v-model="doctor.second_name" type="text" placeholder="Фамилия" />
      <my-input v-model="doctor.third_name" type="text" placeholder="Отчество" />
      <my-input v-model="doctor.phone_number" type="text" placeholder="Номер телефона" />
      <my-input v-model="doctor.experience" type="text" placeholder="Опыт(кол-во лет)" />
      <my-input v-model="doctor.areas_list" type="text" placeholder="Участки" />
      

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
        isFormVisible: true, // Флаг для отображения формы
      };
    },
    methods: {
      async createDoctor() {
        try {
          // Преобразование строковых данных в массив объектов
          this.doctor.areas_list = this.doctor.areas_list
            .split(",")
            .map(item => ({ id: Number(item.trim()) }));
  
          // Отправка данных на сервер
          const response = await axios.post(
            "http://127.0.0.1:8000/doctor/add_new",
            this.doctor,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
            
          );
          console.log(response.status);
          if (response.status === 200) {
        // Успешное создание доктора
        window.location.reload(); // Перезагрузка страницы
      }
  
          this.$emit("create", this.doctor); // Передаём данные родителю
         this.$emit("update:show", false);
  
          alert("Доктор успешно добавлен!");
        } catch (error) {
          console.error("Ошибка создания доктора:", error);
          if (error.response && error.response.data) {
            console.error("Детали ошибки:", error.response.data);
          }
          alert("Ошибка при добавлении доктора. Проверьте данные и попробуйте снова.");
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
  