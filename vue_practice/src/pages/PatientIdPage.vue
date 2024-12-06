<template>
  <div>
    <h1>
      ЭТО СТРАНИЦА ОСМОТРОВ ПАЦИЕНТА С ID = {{ $route.params.id }} (СВЯЗАТЬ С БД
      ЧЕРЕЗ ТАБЛИЦУ ОСМОТРОВj)
    </h1>
  </div>
  <checkup-list :checkups="checkups" @remove="removeCheckup" v-if="!isCheckupsLoading" />
  <div v-else>Идет загрузка...</div>
</template>
<script>
//   import PostForm from "@/Components/PostForm";
import CheckupList from "@/Components/CheckupList.vue";
import axios from "axios";

//   import MySelect from "@/Components/UI/MySelect";
//   import MyButton from "@/Components/UI/MyButton.vue";

export default {
  components: {
    CheckupList,
  },
  data() {
    return {
      checkups: [],
      dialogVisible: false,
      isCheckupsLoading: false,
      selectedSort: "",
      page: 1,
      limit: 3,
      totalPages: 0,
    };
  },
  methods: {
    createCheckup(checkup) {
      this.checkups.push(checkup);
      this.dialogVisible = false;
    },
    removeCheckup(checkup) {
      this.checkups = this.checkups.filter((p) => p.id !== checkup.id);
    },
    showDialog() {
      this.dialogVisible = true;
    },
    changePage(pageNumber) {
      this.page = pageNumber;
      this.fetchCheckups();
    },
    async fetchCheckups() {
      try {
        this.isCheckupsLoading = true;
        const response = await axios.get(
          `http://127.0.0.1:8000/check_up/get_all_checkups_of/${this.$route.params.id}`,
          {
            params: {
 
            },
          }
        );
        this.totalPages = Math.ceil(
          response.headers["x-total-count"] / this.limit
        );
        this.checkups = response.data;
      } catch (e) {
        alert("Ошибка при получении пациентов");
      } finally {
        this.isCheckupsLoading = false;
      }
    },
  },
  mounted() {
    console.log(this.$route.params);
    this.fetchCheckups();
    // this.fetchOptions();
  },
};
</script>
<style scoped></style>
