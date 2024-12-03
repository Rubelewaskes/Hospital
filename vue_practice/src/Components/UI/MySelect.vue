<template>
  <select v-model="selectedValueFIO" @change="changeOption">
    <option disabled value="">ФИО</option>
    <option v-for="option in optionsFIO" :key="option.name">
      {{ option.name }}
    </option>
  </select>
</template>

<script>
export default {
  name: "MySelectFIO",
  props: {
    optionsFIO: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      selectedValueFIO: "",
    };
  },
  methods: {
    changeOption(event) {
      this.$emit("update:modelValue", this.selectedValueFIO);
    },
  },
};
</script>
