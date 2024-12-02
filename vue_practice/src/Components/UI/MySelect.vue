<template>
  <select v-model="selectedValue" @change="changeOption">
    <option disabled value="">ФИО</option>
    <option v-for="option in options" :key="option.name">
      {{ option.name }}
    </option>
  </select>
</template>

<script>
export default {
  name: "MySelect",
  props: {
    options: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      selectedValue: "",
    };
  },
  methods: {
    changeOption(event) {
      this.$emit("update:modelValue", this.selectedValue);
    },
  },
};
</script>
