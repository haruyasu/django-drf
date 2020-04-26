import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Job from "../views/Job.vue";
import JobEditor from "../views/JobEditor.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/job/:id",
    name: "job",
    component: Job,
    props: true
  },
  {
    path: "/editor",
    name: "editor",
    component: JobEditor,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  base: __dirname,
  routes
});

export default router;
