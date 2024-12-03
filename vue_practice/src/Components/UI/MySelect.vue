<template>
  <select class="selectFIO"  v-model="selectedValueFIO" @change="changeOption">
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

<style scoped>
  .selectFIO {
 
 border: 1px solid teal;
 padding: 10px 15px;
 margin: 15px;
  }
 
</style>
