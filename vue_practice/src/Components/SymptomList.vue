<template>
    <div v-if="symptoms && symptoms.length > 0">
      <symptom-item
        v-for="symptom in symptoms"
        :symptom="symptom"
        :key="symptom.id"
        @update="handleUpdate"
         
      />
    </div>
  </template>
  
  <script>
  import SymptomItem from "./SymptomItem.vue";

  
  export default {
    methods: {
      handleUpdate() {
        this.$emit("update"); 
      },
    },
    components: { SymptomItem },
    props: {
        symptoms: {
        type: Array,
        required: true,
        default: () => [], // Установите значение по умолчанию
      },
    },
  };
  </script>
  
  <style scoped></style>
  