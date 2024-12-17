<template>
    <div class="address">
      <div>
        <div><strong>ID: </strong>{{ address.id }}</div>
        <div><strong>Улица: </strong>{{ address.street }}</div>
        <div><strong>Дом: </strong>{{ address.house }}</div>
        <div><strong>Здание: </strong>{{ address.building }}</div>
        <div><strong>Квартира: </strong>{{ address.flat }}</div>
        <div><strong>Участок: </strong>{{ address.area_id }}</div>
        <my-button @click="showDialog">Изменить</my-button>
      </div>
  
      <!-- Диалоговое окно -->
      <div v-if="dialogVisible" class="dialog-overlay">
        <div class="dialog">
          <h3>Изменить данные адреса</h3>
          <form @submit.prevent="submitForm">
            <my-input v-model="formData.id" placeholder="ID" />
            <my-input v-model="formData.street" placeholder="Улица" />
            <my-input v-model="formData.house" placeholder="Дом" />
            <my-input v-model="formData.building" placeholder="Здание" />
            <my-input v-model="formData.flat" placeholder="Квартира" />
            <my-input v-model="formData.area_id" placeholder="Участок" />
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
      address: {
        type: Object,
        required: true,
      },
    },
    data() {
    return {
      dialogVisible: false, // Отображение диалога
      formData: {
        id: this.address.id,
        street: this.address.street,
        house: this.address.house,
        building: this.address.building,
        flat: this.address.flat,
        area_id: this.address.area_id,
      },
    };
  },
  methods: {
    showDialog() {
      this.dialogVisible = true; // Открыть диалог
      this.formData = {
        id: this.address.id,
        street: this.address.street,
        house: this.address.house,
        building: this.address.building,
        flat: this.address.flat,
        area_id: this.address.area_id,
      };
    },
    submitForm() {
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
      this.updateAddress();
      this.closeDialog();
    },
    async updateAddress() {
      try {
        const response = await axios.put(
          `http://127.0.0.1:8000/address/update_one`,
          this.formData,
          {
            
              withCredentials: true,
            
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
  .address {
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
  