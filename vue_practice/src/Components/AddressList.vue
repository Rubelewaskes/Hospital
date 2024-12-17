<template>
    <div v-if="addresses && addresses.length > 0">
      <address-item
        v-for="address in addresses"
        :address="address"
        :key="address.id"
        @update="handleUpdate"
         
      />
    </div>
  </template>
  
  <script>
  import AddressItem from "./AddressItem.vue";

  
  export default {
    methods: {
      handleUpdate() {
        this.$emit("update"); 
      },
    },
    components: { AddressItem },
    props: {
        addresses: {
        type: Array,
        required: true,
        default: () => [], // Установите значение по умолчанию
      },
    },
  };
  </script>
  
  <style scoped></style>
  