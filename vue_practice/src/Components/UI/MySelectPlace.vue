<template>
    <select class="selectPlace" v-model="selectedValuePlace" @change="changeOption">
      <option disabled value="">Места</option>
      <option v-for="option in optionsPlace" :key="option.place">
        {{ option.place }}
      </option>
    </select>
  </template>
  
  <script>
  export default {
    name: "MySelectPlace",
    props: {
      optionsPlace: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {
        selectedValuePlace: "",
      };
    },
    methods: {
      changeOption(event) {
        this.$emit("update:modelValue", this.selectedValuePlace);
      },
    },
  };
  </script>

  <style scoped>
  .selectPlace {
 
 border: 1px solid teal;
 padding: 10px 15px;
 margin: 15px;
  }
 
</style>