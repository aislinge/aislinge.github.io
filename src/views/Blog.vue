<template>
  <div class="container">
    <div v-html="toc" class="toc_nav colorful"></div>
    <i id="top"></i>
    <a href="#top">
      <i id="back_top" class="colorful nf nf-mdi-format_vertical_align_top"></i>
    </a>
    <div class="main">
      <router-link to="/blog" tag="strong" id="back_btn_top">
        <i class="nf nf-fa-arrow_left"></i>
        返回
      </router-link>
      <div class="markdown" v-html="content"></div>
      <router-link to="/blog" tag="strong" id="back_btn_bottom">
        <i class="nf nf-fa-arrow_left"></i>
        返回
      </router-link>
    </div>
  </div>
</template>
<script>
//import "@/assets/theme/github-markdown.css";
import BLOGDATA from "@/assets/data/blog_data.json";
import "@/assets/theme/code.css";

export default {
  name: "Blog",
  data() {
    return {
      content: "",
      toc: "",
    };
  },
  methods: {
    set_content() {
      const id = this.$route.params.id;
      this.content = BLOGDATA[id].content;
    },
    set_toc() {
      const id = this.$route.params.id;
      this.toc = BLOGDATA[id].toc;
    },
  },
  mounted() {
    this.set_toc();
    this.set_content();
  },
};
</script>

<style scoped src="@/assets/theme/blog.css"></style>
<style scoped>
.container {
  position: relative;
}
#back_top {
  width: 40px;
  height: 40px;
  color: #fff;
  font-size: 30px;
  border-radius: 30px;
  background: #fbb;
  display: inline-block;
  border: 1px solid #fbb;
  text-align: center;
  line-height: 40px;
  position: fixed;
  bottom: 90px;
  right: 50px;
}
.main {
  width: 80%;
  margin: 0 auto;
}
.toc_nav {
  top: 60px;
  left: -20px;
  bottom: 100px;
  width: 350px;
  position: fixed;
  overflow: scroll;
  transform: translateX(-320px);
  transition: transform 200ms ease-in;
  border-radius: 5px;
  border: 1px solid #000;
  z-index: 999999999;
}
.toc_nav:hover {
  background: #fdd;
  transform: translateX(0);
}
.toc_nav >>> .toc {
  top: 0;
  left: 0;
  bottom: 0;
  width: calc(100% - 30px);
  border-radius: 5px;
}

.toc_nav >>> li {
  white-space: nowrap;
  line-height: 2em;
  list-style: none;
  max-width: 300px;
  overflow: hidden;
  text-overflow: clip;
}
.toc_nav >>> li a {
  color: #f00;
  text-decoration: none;
  display: inline-block;
}
.toc_nav >>> .toc > ul > li > ul > li::before {
  color: #f00;
  content: "\f138";
  margin-right: 10px;
}
#back_btn_top {
  background: red;
  margin-top: 30px;
  width: 100px;
  text-align: center;
  display: block;
  border-radius: 30px;
  cursor: pointer;
  color: #fff;
}
#back_btn_top:hover {
  cursor: pointer;
}
#back_btn_top > .nf {
  margin-right: 10px;
}
#back_btn_bottom {
  margin-top: 30px;
  background: red;
  width: 100px;
  text-align: center;
  display: block;
  border-radius: 30px;
  color: #fff;
  cursor: pointer;
}
#back_btn_bottom:hover {
  cursor: pointer;
}
#back_btn_bottom > .nf {
  margin-right: 10px;
}
</style>
