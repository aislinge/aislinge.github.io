<template>
  <div class="ui container">
    <div v-for="(content, id) in contents" :key="id">
      <div v-html="content['content']"></div>
      <p id="author">作者： {{ content["author"][0] }}</p>
      <p id="date">编辑日期： {{ content["modified_date"][0] }}</p>
    </div>
  </div>
</template>
<script>
import JSONDATA from "@/assets/data/about.json";

export default {
  name: "About",
  data() {
    return {
      contents: JSONDATA,
    };
  },
  components: {},
  mounted() {
    console.log(this.content);
  },
};
</script>
<style  scoped>
.container {
  width: 70%;
  border-radius: 5px;
  padding: 20px 0;
}
.container >>> p:first-child {
  text-indent: 0;
}
.container >>> p {
  font-family: "YRDM";
  font-size: 1.2em;
  text-indent: 2em;
  line-height: 2em;
}
#author,
#date {
  text-align: right;
}
#author {
  margin-top: 60px;
}
</style>

