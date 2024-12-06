<template>
    <div class="checkup">
      <div>
        <div><strong>ФИО: </strong>{{ checkup.doctor_FIO }} </div>
        <div><strong>Место: </strong>{{ checkup.place }}</div>
      </div>
      <div class="post__btns">
        <my-button @click="$emit('remove', checkup)">Удалить</my-button>
      </div>
    </div>
  </template> 
  
  <script>
  export default {
    props: {
      checkup: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .checkup {
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
  