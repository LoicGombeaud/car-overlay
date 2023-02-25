import { createRouter, createWebHistory } from "vue-router"
import Home from "./components/Home.vue"
import Editor from "./components/Editor.vue"

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/editor",
      component: Editor,
    },
    {
      path: "/:pathMatch(.*)",
      redirect: "/",
    },
  ]
})
