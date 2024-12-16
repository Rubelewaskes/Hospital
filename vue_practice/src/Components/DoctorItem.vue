<template>
  <div class="doctor">
    <div>
      <div><strong>ID: </strong>{{ doctor.doctor_id }}</div>
      <div><strong>Имя: </strong>{{ doctor.first_name }}</div>
      <div><strong>Фамилия: </strong>{{ doctor.second_name }}</div>
      <div><strong>Отчество: </strong>{{ doctor.third_name }}</div>
      <div><strong>Телефон: </strong>{{ doctor.phone_number }}</div>
      <div><strong>Опыт: </strong>{{ doctor.experience }} лет</div>
      <div><strong>Список участков: </strong>{{ doctor.areas_list }}</div>
      <my-button @click="showDialog">Изменить</my-button>
    </div>

    <!-- Диалоговое окно -->
    <div v-if="dialogVisible" class="dialog-overlay">
      <div class="dialog">
        <h3>Изменить данные врача</h3>
        <form @submit.prevent="submitForm">
          <my-input v-model="formData.doctor_id" placeholder="ID" />
          <my-input v-model="formData.first_name" placeholder="Имя" />
          <my-input v-model="formData.second_name" placeholder="Фамилия" />
          <my-input v-model="formData.third_name" placeholder="Отчество" />
          <my-input v-model="formData.phone_number" placeholder="Телефон" />
          <my-input v-model="formData.experience" placeholder="Опыт (лет)" />
          <my-input
            v-model="formData.areas_list" 
            placeholder="Список участков (через запятую)"
          />
          <div class="btns">
          <my-button type="submit">Сохранить</my-button>
          <my-button @click="closeDialog" type="button">Отмена</my-button>
        </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    doctor: {
      type: Object,
      required: true,
    },
  },
  data() {
  return {
    dialogVisible: false, // Отображение диалога
    formData: {
      id: this.doctor.doctor_id, // Добавляем ID
      first_name: this.doctor.first_name,
      second_name: this.doctor.second_name,
      third_name: this.doctor.third_name,
      phone_number: this.doctor.phone_number,
      experience: this.doctor.experience,
      areas_list: "", // Поле остается пустым для отображения placeholder
    },
  };
},
methods: {
  showDialog() {
    this.dialogVisible = true; // Открыть диалог
    this.formData = {
      id: this.doctor.doctor_id,
      first_name: this.doctor.first_name,
      second_name: this.doctor.second_name,
      third_name: this.doctor.third_name,
      phone_number: this.doctor.phone_number,
      experience: this.doctor.experience,
      areas_list: "", // Поле остаётся пустым
    };
  },
  submitForm() {
    // Преобразуем строку areas_list обратно в массив объектов { id: <number> }
    if (this.formData.areas_list.trim() !== "") {
      this.formData.areas_list = this.formData.areas_list
        .split(",") // Разделяем по запятой
        .map((id) => {
          return { id: parseInt(id.trim(), 10) }; // Приводим к числу и оборачиваем в объект
        });
    } else {
      this.formData.areas_list = []; // Если пустая строка, отправляем пустой массив
    }
    console.log("Преобразованный areas_list:", this.formData.areas_list);
    console.log("Отправка формы с данными:", this.formData);
    this.updateDoctor();
    this.closeDialog();
  },
  async updateDoctor() {
    try {
      const response = await axios.put(
        `http://127.0.0.1:8000/doctor/update/`,
        this.formData, // Используем данные из формы
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      this.$emit("update"); // Генерация события для обновления    
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
  closeDialog() {
    this.dialogVisible = false; // Закрыть диалог
  },
},


};
</script>

<style scoped>
.doctor {
  padding: 15px;
  border: 2px solid teal;
  margin: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}
form {
  display: flex;
  flex-direction: column;
}
my-button {
  margin-top: 10px;
}
.btns{
 display:flex;
 justify-content: space-between;
}
</style>
