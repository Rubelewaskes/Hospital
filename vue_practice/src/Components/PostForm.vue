<!-- МОДАЛЬНОЕ ОКНО -->
<template>
  <form @submit.prevent="createPost">
    <h4>Новый осмотр</h4>

    <my-input v-model="post.place" type="text" placeholder="Место осмотра" />
    <my-input v-model="post.date" type="text" placeholder="Дата осмотра" />
    <my-input
      v-model="post.doctor"
      type="text"
      placeholder="Врач проводивший осмотр"
    />
    <div>
      <!-- Выпадающий список для ФИО-->
      <my-select v-model="selectedOption" :options="options" />
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
      options: [], // Данные для выпадающего списка
      selectedOption: "", // Выбранное значение из выпадающего списка
    };
  },
  methods: {
    async fetchOptions() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/patient/get_all"
        );
        console.log("Полученные данные:", response.data);

        // Убедитесь, что используете данные с правильным полем
        this.options = response.data.map((item) => ({
          name: `${item.first_name} ${item.second_name} ${item.third_name}`, // Имя опции для отображения
        }));
      } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
      }
    },
    createPost() {
      // Добавляем выбранное значение в объект post
      this.post.selectedOption = this.selectedOption;

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
      this.selectedOption = ""; // Очистка выбранной опции
    },
  },
  mounted() {
    this.fetchOptions(); // Загрузка данных при монтировании
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>
