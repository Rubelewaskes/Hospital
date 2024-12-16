<template>
  <div v-if="doctors.length > 0">
    <doctor-item
      v-for="doctor in doctors"
      :doctor="doctor"
      :key="doctor.id"
      @update="handleUpdate"
       
    />
  </div>
</template>

<script>
import DoctorItem from "./DoctorItem.vue";

export default {
  methods: {
    handleUpdate() {
      this.$emit("update"); // Поднимаем событие дальше к AdminAllDoctors
    },
  },
  components: { DoctorItem },
  props: {
    doctors: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped></style>
