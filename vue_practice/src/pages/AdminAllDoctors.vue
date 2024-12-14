<template>
  <div>
    <div class="chekup">
      <h1 v-if="doctors.length > 0">Список врачей</h1>
      <h2 v-else style="color: red">Отсутствуют врачи</h2>
      <div class="btn">
          <my-button @click="showDialog"> Добавить врача </my-button>
        </div>
    </div>
    <doctor-list
      :doctors="doctors"
      @change="changeDoctor"
      v-if="!isDoctorsLoading"
    />

    <div v-else>Идет загрузка...</div>

    <my-dialog v-model:show="dialogVisible">
  <doctor-create-form @create="createDoctor" />
</my-dialog>

  </div>

  <!-- <div>
      <my-select v-model="selectedOption" :options="options" />
    </div> -->
  <div class="page__wrapper">
    <div
      class="page"
      v-for="pageNumber in totalPages"
      :key="pageNumber"
      :class="{ 'current-page': page === pageNumber }"
      @click="changePage(pageNumber)"
    >
      {{ pageNumber }}
    </div>
  </div>
</template>

<script>
// import PostForm from "@/Components/PostForm";
import DoctorList from "@/Components/DoctorList";
import axios from "axios";
import DoctorCreateForm from "@/Components/DoctorCreateForm.vue";
// import MySelect from "@/Components/UI/MySelect";
// import MyButton from "@/Components/UI/MyButton.vue";

export default {
  components: {
    // PostForm,
    DoctorList,
    DoctorCreateForm,
    // MySelect,
  },
  data() {
    return {
      doctors: [],
      dialogVisible: false,
      isDoctorsLoading: false,
      selectedSort: "",
      page: 1,
      limit: 3,
      totalPages: 0,
      // options: [], // Данные для выпадающего списка
      // selectedOption: "", // Выбранное значение
    };
  },
  methods: {
    createDoctor(doctor) {
      this.doctors.push(doctor);
      this.dialogVisible = false;
    },
    removeDoctor(doctor) {
      this.doctors = this.doctors.filter((p) => p.id !== doctor.id);
    },
    showDialog() {
      this.dialogVisible = true;
    },
    changePage(pageNumber) {
      this.page = pageNumber;
      this.fetchDoctors();
    },
    async fetchDoctors() {
      try {
        this.isDoctorsLoading = true;
        const response = await axios.get(
          "http://127.0.0.1:8000/doctor/get_all",
          {
            params: {
              _page: this.page,
              _limit: this.limit,
            },
          }
        );
        this.totalPages = Math.ceil(
          response.headers["x-total-count"] / this.limit
        );
        this.doctors = response.data;
      } catch (e) {
        alert("Ошибка при получении пациентов");
      } finally {
        this.isDoctorsLoading = false;
      }
    },
  },
  mounted() {
    this.fetchDoctors();
  },
};
</script>

<style>
.chekup {
  display: flex;
  justify-content: space-between;
  margin: 0px 15px;
}

.app__btns {
  margin: 15px 0px;
  display: flex;
  justify-content: space-between;
}

.nav {
  width: 100%;
  height: 50px;
  background-color: teal;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
}

.nav-in {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  width: 100%;
}

.right-group {
  display: flex;
  align-items: center;
  gap: 15px;
}

.page__wrapper {
  display: flex;
  margin-left: 15px;
  margin-top: 15px;
}

.page {
  border: 1px solid black;
  padding: 10px;
}

.current-page {
  border: 2px solid teal;
}
</style>
