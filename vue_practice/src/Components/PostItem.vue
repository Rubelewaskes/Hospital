<template>
  <div class="post">
    <div>
      <div><strong>ФИО: </strong>{{ post.first_name }} {{ post.second_name }} {{ post.third_name }}</div>
      <div><strong>Дата рождения: </strong>{{ post.born_date }}</div>
      <div><strong>ID: </strong>{{ post.id }}</div>
    </div>
    <div class="post__btns">
      <my-button class="look_up" @click="$router.push(`/patients/${post.id}`)" >Просмотреть</my-button>
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

.look_up {
  margin-right: 10px;
}
</style>
