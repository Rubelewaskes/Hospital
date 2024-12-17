<template>
  <div v-if="posts.length > 0">
    <!-- <h3>Список пациентов</h3> -->
    <post-item
      v-for="post in posts"
      :post="post"
      :key="post.patient_id"
      @remove="$emit('remove', post)"
    />
  </div>
  <!-- <h2 v-else style="color: red">Отсутствуют пациенты</h2> -->
</template>

<script>
import PostItem from "./PostItem.vue";

export default {
  components: { PostItem },
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped></style>
