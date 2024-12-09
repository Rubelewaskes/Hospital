<!-- МОДАЛЬНОЕ ОКНО -->
<template>
  <form @submit.prevent="createPost">
    <h4>Новый осмотр</h4>

 
    <my-selectPlace
      
      :optionsPlace="optionsPlace"
      />
      <my-input
      v-model="post.check_up_place_id"
      type="text"
      placeholder="Место осмотра"
    />
    <my-input
      v-model="post.check_up_date"
      type="text"
      placeholder="Дата осмотра"
    />
    <my-input
      v-model="post.doctor_id"
      type="text"
      placeholder="Врач проводивший осмотр"
    />

    <!-- Выпадающий список для ФИО-->
    <my-input v-model="post.patient_id" type="text" placeholder="id пациента" />

    <my-input
      v-model="symptomsInput"
      type="text"
      placeholder="Симптомы (через запятую)"
    />
    <my-input v-model="post.diagnosis_id" type="text" placeholder="Диагноз" />
    <my-input
      v-model="post.prescription"
      type="text"
      placeholder="Предписание"
    />
    <my-button
      class="btn"
      style="align-self: flex-end; margin-top: 15px"
      type="submit"
    >
      Создать
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
  data() {
    return {
      post: {
        check_up_place_id: "",
        check_up_date: "",
        doctor_id: "",
        patient_id: "",
        diagnosis_id: "",
        prescription: "",
        symptoms_list: [],
        
        
      },
      symptomsInput: "", // Для ввода строки симптомов
      optionsFIO: [], // Данные для выпадающего списка ФИО
      selectedOptionFIO: "", // Выбранное значение из выпадающего списка
      optionsPlace: [], // Данные для выпадающего списка Места осмотра
      selectedOptionPlace: "",
    };
  },
  methods: {
    async fetchOptionsFIO() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/patient/get_all"
        );
        console.log("Полученные данные Patients:", response.data);

        // Убедитесь, что используете данные с правильным полем
        this.optionsFIO = response.data.map((item) => ({
          name: `${item.place}`, // Имя опции для отображения
        }));
      } catch (error) {
        console.error("Ошибка при загрузке данных Patients:", error);
      }
    },
    async fetchOptionsPlace() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/check_up/get_all_places"
        );
        console.log("Полученные данные Places:", response.data);

        // Убедитесь, что используете данные с правильным полем
        this.optionsPlace = response.data.map((item) => ({
          place: `${item.place}`, // Имя опции для отображения
        }));
      } catch (error) {
        console.error("Ошибка при загрузке данных Places:", error);
      }
    },
    async submitForm() {
        if (!this.post.check_up_place_id) {
    alert("Место осмотра не выбрано!");
    return;
  }
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/check_up/add_new",
          this.post, // Убедитесь, что данные имеют нужную серверу структуру
          {
            headers: {
              "Content-Type": "application/json", // Заголовок для JSON
            },
          }
        );
        alert("Данные успешно отправлены!");
        console.log("Ответ сервера:", response.data);
      } catch (error) {
        console.error("Ошибка отправки:", error);
        if (error.response) {
          console.error("Ответ сервера:", error.response.data);
        }
        alert("Произошла ошибка. Попробуйте снова.");
      }
    },

    createPost() {
      // Преобразуем строку симптомов в массив объектов
      this.post.symptoms_list = this.symptomsInput
        .split(",") // Разделяем по запятой
        .map((item) => ({
          id: Date.now(), // Уникальный идентификатор (замените на нужный)
          name: item.trim(), // Имя симптома
        }));

      console.log(
        "Данные формы (массив объектов симптомов):",
        this.post.symptoms_list
      );

      // Добавляем выбранное значение в объект post
      this.post.selectedOptionFIO = this.selectedOptionFIO;
      this.post.selectedOptionPlace = this.selectedOptionPlace;

      console.log("Данные формы:", this.post);
      this.post.id = Date.now(); // Генерация уникального ID
      this.$emit("create", this.post); // Передача данных в родительский компонент

      this.submitForm();

      // Сброс формы
      this.symptomsInput = "";
      this.post = {
        check_up_place_id: "",
        check_up_date: "",
        doctor_id: "",
        patient_id: "",
        diagnosis_id: "",
        prescription: "",
        symptoms_list: [],
      };
      this.selectedOptionFIO = ""; // Очистка выбранной опции
      this.selectedOptionPlace = "";
    },
  },

  mounted() {
    this.fetchOptionsFIO();
    this.fetchOptionsPlace(); // Загрузка данных при монтировании
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>
