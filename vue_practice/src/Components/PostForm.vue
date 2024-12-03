<!-- МОДАЛЬНОЕ ОКНО -->
<template>
  <form @submit.prevent="createPost">
    <h4>Новый осмотр</h4>

    <my-selectPlace v-model="selectedOptionPlace" :optionsPlace="optionsPlace" />
    <my-input v-model="post.date" type="text" placeholder="Дата осмотра" />
    <my-input
      v-model="post.doctor"
      type="text"
      placeholder="Врач проводивший осмотр"
    />
    <div>
      <!-- Выпадающий список для ФИО-->
      <my-selectFIO v-model="selectedOptionFIO" :optionsFIO="optionsFIO" />
    </div>
    <my-input v-model="post.symptoms" type="text" placeholder="Симптомы" />
    <my-input v-model="post.diagnosis" type="text" placeholder="Диагноз" />
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
        place: "",
        date: "",
        doctor: "",
        diagnosis: "",
        prescription: "",
        symptoms: "",
      },
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
          name: `${item.first_name} ${item.second_name} ${item.third_name}`, // Имя опции для отображения
        }));
      } catch (error) {
        console.error("Ошибка при загрузке данных Patients:", error);
      }
    },
    async fetchOptionsPlace() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/check_up/get_check_up_places"
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
    createPost() {
      // Добавляем выбранное значение в объект post
      this.post.selectedOptionFIO = this.selectedOptionFIO;
      this.post.selectedOptionPlace = this.selectedOptionPlace;

      console.log("Данные формы:", this.post);
      this.post.id = Date.now(); // Генерация уникального ID
      this.$emit("create", this.post); // Передача данных в родительский компонент

      // Сброс формы
      this.post = {
        place: "",
        date: "",
        doctor: "",
        diagnosis: "",
        prescription: "",
        symptoms: "",
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
