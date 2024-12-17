<template>
    <div v-if="areas && areas.length > 0">
      <area-item
        v-for="area in areas"
        :area="area"
        :key="area.id"
        @update="handleUpdate"
         
      />
    </div>
  </template>
  
  <script>
  import AreaItem from "./AreaItem.vue";

  
  export default {
    methods: {
      handleUpdate() {
        this.$emit("update"); 
      },
    },
    components: { AreaItem },
    props: {
        areas: {
        type: Array,
        required: true,
        default: () => [], // Установите значение по умолчанию
      },
    },
  };
  </script>
  
  <style scoped></style>
  