<template>
    <input class="input" :value="modelValue" @input="updateInput" type="text">
  </template>
  
  <script>
  export default {
    name: 'my-input',
    props: {
      modelValue: [String, Number]
    },
    methods: {
      updateInput(event) {
        this.$emit('update:modelValue', event.target.value);
      }
    }
  };
  </script>
  
  <style scoped>
  .input {
    border: 1px solid teal;
    padding: 10px 15px;
    margin-bottom: 10px;
    margin-top: 10px; 
    width: 100%; 
    box-sizing: border-box; 
  }
  </style>
  