<template>
    <div class="area">
      <div>
        <div><strong>ID: </strong>{{ area.id }}</div>
      </div>
  
      <!-- Диалоговое окно -->
      <div v-if="dialogVisible" class="dialog-overlay">
        <div class="dialog">
          <form @submit.prevent="submitForm">
            <my-input v-model="formData.id" placeholder="ID" />
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
  
import axios from 'axios';

  export default {
    props: {
      area: {
        type: Object,
        required: true,
      },
    },
    data() {
    return {
      dialogVisible: false, // Отображение диалога
      formData: {
        id: this.area.id,
      },
    };
  },
  methods: {
    showDialog() {
      this.dialogVisible = true; // Открыть диалог
      this.formData = {
        id: this.area.id,
      };
    },
    submitForm() {
      // Преобразуем строку areas_list обратно в массив объектов { id: <number> }
        if (this.formData.areas_list?.trim()) {
  this.formData.areas_list = this.formData.areas_list
    .split(",")
    .map((id) => {
      return { id: parseInt(id.trim(), 10) };
    });
} else {
  this.formData.areas_list = [];
}

      console.log("Преобразованный areas_list:", this.formData.areas_list);
      console.log("Отправка формы с данными:", this.formData);
      this.closeDialog();
    },
    closeDialog() {
      this.dialogVisible = false; // Закрыть диалог
    },
  },
  
  
  };
  </script>
  
  <style scoped>
  .area {
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
  