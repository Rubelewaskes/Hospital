  <!-- МОДАЛЬНОЕ ОКНО -->
<template>
  <form @submit.prevent="createPost"> 
    <h4>Новый осмотр</h4>
    <my-input v-model="post.title" type="text" placeholder="Название" />
    <my-input v-model="post.body" type="text" placeholder="Описание" />
    <my-button
      class="btn"
      style="align-self: flex-end; margin-top: 15px"
      type="submit"
    >
      Создать
    </my-button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      post: {
        title: "",
        body: "",
      },
    };
  },
  methods: {
    createPost() {
      console.log("Форма отправлена", this.post);
      this.post.id = Date.now(); // Генерация ID для нового поста
      this.$emit("create", this.post); // Передача данных в родительский компонент
      this.post = {
        title: "",
        body: "",
      }; // Очистка формы
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>