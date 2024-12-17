<template lang="html">
  <div v-if="isFormVisible">
    <form @submit.prevent="createDiagnosis">
      <h4>Добавление диагноза</h4>

      <my-input v-model="diagnosis.id" type="text" placeholder="ID:" />
      <my-input
        v-model="diagnosis.name"
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
      isFormVisible: true, // Флаг для отображения формы
    };
  },
  methods: {
    async createDiagnosis() {
      try {
        // Отправка данных на сервер
        const response = await axios.post(
          "http://127.0.0.1:8000/diagnosis/add_new",
          this.diagnosis,
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

        this.$emit("create", this.diagnosis); // Передаём данные родителю
        this.$emit("update:show", false);

        alert("Диагноз успешно добавлен!");
      } catch (error) {
        console.error("Ошибка создания диагноза:", error);
        if (error.response && error.response.data) {
          console.error("Детали ошибки:", error.response.data);
        }
        alert(
          "Ошибка при добавлении диагноза. Проверьте данные и попробуйте снова."
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
