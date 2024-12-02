<template>
  <div class="post">
    <div>
      <div><strong>ФИО</strong>{{ post.first_name }} </div>
      <div><strong>Описание-</strong>{{ post.body }}</div>
    </div>
    <div class="post__btns">
      <my-button @click="$emit('remove', post)">Удалить</my-button>
    </div>
  </div>
</template>

<script>
 

export default {
 
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
