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
      <my-button @click="showDialog"> Изменить </my-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    doctor: {
      type: Object,
      required: true,
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

.look_up {
  margin-right: 10px;
}
</style>
