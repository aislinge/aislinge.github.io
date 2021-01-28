import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home";
import BlogList from "@/views/BlogList";
import Repo from "@/views/Repo";
import About from "@/views/About";
import Love from "@/views/Love";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    meta: {
      title: "首页"
    }
  },
  {
    path: "/blog",
    name: "Blog_List",
    component: BlogList,
    meta: {
      title: "文章"
    }
  },
  {
    path: "/blog/:id",
    component: () => import("@/views/Blog"),
    meta: {
      title: "文章"
    }
  },
  {
    path: "/repo",
    name: "Repo",
    component: Repo,
    meta: {
      title: "项目"
    }
  },
  {
    path: "/about",
    name: "About",
    component: About,
    meta: {
      title: "关于"
    }
  },
  {
    path: "/NIXIAK",
    name: "Love",
    component: Love,
    meta: {
      title: "Flipped"
    }
  }
];

const router = new VueRouter({
  mode: "history",
  linkActiveClass: "active",
  routes: routes
});

router.beforeEach((to, from, next) => {
  document.title = "Aislinge - " + to.matched[0]?.meta.title;
  next();
});

export default router;
