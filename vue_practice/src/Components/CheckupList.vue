<template>
  <div v-if="checkups.length > 0">
    <!-- <h3>Список осмотров</h3> -->
    <post-item
      v-for="checkup in checkups"
      :checkup="checkup"
      :key="checkup.id"
      @remove="$emit('remove', checkup)"
    />
  </div>
</template>

<script>
import CheckupItem from "./CheckupItem.vue";

export default {
  components: { CheckupItem },
  props: {
    checkups: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped></style>
