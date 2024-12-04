import { createApp } from "vue";
import App from "./App.vue";
import components from "@/Components/UI";
import router from "./router/router";

const app = createApp(App);

components.forEach((component) => {
  app.component(component.name, component);
});

app.use(router);
app.mount("#app");
