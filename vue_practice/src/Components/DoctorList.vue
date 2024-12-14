<template>
  <div v-if="doctors.length > 0">
    <doctor-item
      v-for="doctor in doctors"
      :doctor="doctor"
      :key="doctor.id"
      @change="$emit('change', doctor)"
    />
  </div>
</template>

<script>
import DoctorItem from "./DoctorItem.vue";

export default {
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
