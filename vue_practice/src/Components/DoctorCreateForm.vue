<template lang="html">
  <div v-if="isFormVisible">
    <form @submit.prevent="createDoctor">
      <h4>Добавление доктора</h4>

      <!-- Поля доктора -->
      <my-input v-model="doctor.first_name" type="text" placeholder="Имя" />
      <my-input v-model="doctor.second_name" type="text" placeholder="Фамилия" />
      <my-input v-model="doctor.third_name" type="text" placeholder="Отчество" />
      <my-input v-model="doctor.phone_number" type="text" placeholder="Номер телефона" />
      <my-input v-model="doctor.experience" type="number" placeholder="Опыт (лет)" />

      <!-- Поле участков (через запятую) -->
      <my-input
        v-model="areasInput"
        type="text"
        placeholder="Участки (ID через запятую)"
      />

      <!-- Поля пользователя -->
      <my-input
        v-model="doctor.user_create.email"
        type="email"
        placeholder="Email пользователя"
      />
      <my-input
        v-model="doctor.user_create.password"
        type="password"
        placeholder="Пароль"
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
import axios from "axios";

export default {
  data() {
    return {
      doctor: {
        first_name: "",
        second_name: "",
        third_name: "",
        phone_number: "",
        experience: 0,
        areas_list: [], // Список участков как массив объектов
        user_create: {
          email: "",
          password: "",
          is_active: true,
          is_superuser: false,
          is_verified: false, // Новое поле для верификации
          is_doctor: true,
        },
      },
      areasInput: "", // Строка для ввода участков через запятую
      isFormVisible: true, // Флаг для отображения формы
    };
  },
  methods: {
    async createDoctor() {
      try {
        // Преобразование строки участков в массив объектов
        if (this.areasInput.trim()) {
          this.doctor.areas_list = this.areasInput
            .split(",")
            .map((id) => ({ id: parseInt(id.trim(), 10) }));
        } else {
          this.doctor.areas_list = [];
        }

        // Отправка данных на сервер
        const response = await axios.post(
          "http://127.0.0.1:8000/doctor/add_new",
          this.doctor,
          {
            withCredentials: true,
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (response.status === 200) {
          alert("Доктор успешно добавлен!");
          this.$emit("create", this.doctor); // Уведомляем родителя
          this.$emit("update:show", false); // Закрываем форму
          window.location.reload(); // Перезагрузка страницы
        }
      } catch (error) {
        console.error("Ошибка создания доктора:", error);
        if (error.response?.data) {
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
