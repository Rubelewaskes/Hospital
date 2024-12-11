<template>
  <select
    class="selectPlace"
    v-model="selectedValuePlace"
    @change="changeOption"
  >
    <option disabled value="">Место осмотра</option>
    <option
      v-for="option in optionsPlace"
      :key="option.value"
      :value="option.value"
      v-if="optionsPlace.length"
    >
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
    modelValue: {
      type: [String, Number],
      default: "",
    },
  },
  data() {
    return {
      selectedValuePlace: this.modelValue, // Инициализируем значением props.modelValue
    };
  },
  watch: {
    selectedValuePlace(newValue) {
      this.$emit("update:modelValue", newValue); // Обновляем значение через v-model
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
