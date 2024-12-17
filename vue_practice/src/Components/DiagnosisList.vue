<template>
    <div v-if="diagnoses && diagnoses.length > 0">
      <diagnosis-item
        v-for="diagnosis in diagnoses"
        :diagnosis="diagnosis"
        :key="diagnosis.id"
        @update="handleUpdate"
         
      />
    </div>
  </template>
  
  <script>
  import DiagnosisItem from "./DiagnosisItem.vue";

  
  export default {
    methods: {
      handleUpdate() {
        this.$emit("update"); 
      },
    },
    components: { DiagnosisItem },
    props: {
      diagnoses: {
        type: Array,
        required: true,
        default: () => [], // Установите значение по умолчанию
      },
    },
  };
  </script>
  
  <style scoped></style>
  