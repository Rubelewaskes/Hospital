<template>
  <select class="selectFIO" v-model="selectedValueFIO" @change="changeOption">
    <option disabled value="">ФИО</option>
    <option
      v-for="option in optionsFIO"
      :key="option.value"
      :value="option.value"
    >
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
    modelValue: {
      type: [String, Number], // Тип значения может быть string или number в зависимости от данных
      default: "",
    },
  },
  data() {
    return {
      selectedValueFIO: this.modelValue, // Инициализируем значением props.modelValue
    };
  },
  watch: {
    selectedValueFIO(newValue) {
      this.$emit("update:modelValue", newValue); // Обновляем значение через v-model
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
