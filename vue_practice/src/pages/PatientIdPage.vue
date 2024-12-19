<template>
  <div>
    <div class="header-container" v-if="checkups.length > 0">
      <!-- Стрелочка для возврата -->
      <span class="back-arrow" @click="backToPatients" style="cursor: pointer;">←</span>
      <!-- Заголовок -->
      <h1 class="checkup_list">Список осмотров</h1>
    </div>
    <h2 v-else style="color: red">Отсутствуют осмотры</h2>

    <checkup-list
      :checkups="checkups"
      @remove="removeCheckup"
      v-if="!isCheckupsLoading"
    />
    <div v-else>Идет загрузка...</div>
  </div>
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
      this.checkups = this.checkups.filter(
        (c) => c.check_up_id !== checkup.check_up_id
      );
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
          `http://127.0.0.1:8000/check_up/get_all_checkups_of/${this.$route.params.patient_id}`,
          {
            
            withCredentials: true,
          
            params: {},
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
    backToPatients() {
      this.$router.push("/patientsAdmin");
    },
  },
  mounted() {
    console.log(this.$route.params);
    this.fetchCheckups();
    // this.fetchOptions();
  },
};
</script>
<style scoped>
.header-container {
  display: flex;
  align-items: center; /* Выравнивание по вертикали */
  gap: 10px; /* Расстояние между стрелкой и заголовком */
}

.back-arrow {
  font-size: 1.5rem;
  color: teal;
  margin-left: 15px;
}

.back-arrow:hover {
  color: darkblue; /* Цвет стрелочки при наведении */
}

.checkup_list {
  margin: 0; /* Убираем отступы */
  font-size: 1.5rem;
  color: black;
}
</style>
