<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-lg-4 g-4">
      <div class="col" v-for="(blog, id) in blogs" :key="id">
        <div class="card colorful h-100">
          <div class="card-header" alt="cover">
            <h5>
              {{ blog.title[0] }}
            </h5>
            <hr />
            <span
              class="badge rounded-pill"
              v-for="(tag, id) in blog.tags"
              :key="id"
            >
              {{ tag }}
            </span>
          </div>
          <div class="card-body">
            <!-- <h5 class="card-title">{{ repo['name'] }}</h5> -->
            <p class="card-text">
              {{
                blog.description[0] ? blog.description[0] : "这个项目没有介绍"
              }}
            </p>
          </div>
          <div class="card-footer d-flex justify-content-between">
            <small class="text">{{ computedTime(blog.date[0]) }}</small>
            <router-link class="link" :to="'/blog/' + id">文章页面</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
const moment = require("moment");

moment.locale("zh_CN");

let today = moment();
import BLOGDATA from "../assets/data/blog_data.json";

export default {
  name: "BlogList",
  data() {
    return {
      blogs: BLOGDATA,
    };
  },
  methods: {
    computedTime(time) {
      let seconds = today.diff(moment(time), "seconds");
      if (seconds < 60) {
        return seconds + "秒以前";
      }
      let minutes = today.diff(moment(time), "minutes");
      if (minutes < 60) {
        return minutes + "分以前";
      }
      let hours = today.diff(moment(time), "hours");
      if (hours < 12) {
        console.log(hours);
        return hours + "时以前";
      }
      let days = today.diff(moment(time), "days");
      if (days <= 30) {
        console.log(days);
        return days + "天以前";
      }
      let months = today.diff(moment(time), "months");
      if (months >= 1 && months <= 12) {
        return months + "月以前";
      }
      let years = today.diff(moment(time), "years");
      if (years >= 1) {
        return years + "年以前";
      }
    },
  },
  mounted() {
    console.log(BLOGDATA);
    console.log(this.blog.index);
  },
};
</script>

<style scoped>
* {
  font-family: "SCR";
}
.card >>> .card-header {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  color: #bf0404;
  display: block;
  border: none;
  background: none;
}
.card >>> .badge {
  color: #fff;
  margin-right: 10px;
  background: #bf0404;
}
div.row {
  margin-top: 20px;
}
.list-group-item {
  margin-top: 30px;
}
.card-text {
  color: #000;
}
.card-footer {
  line-height: 30px;
  color: #f00;
  border: none;
  background: none;
}
.card-footer >>> small {
  color: #333;
}

.btn {
  font-weight: bold;
  color: #f00;
  font-size: 14px;
}
a::before {
  content: "\f0a9";
  color: #f00;
  font-family: "SCR", "NFR";
  padding-right: 10px;
  margin-left: 10px;
  text-decoration: none;
}

a {
  color: #f00;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
.card .card-header > h5::before {
  content: "\f401";
  color: #bf0404;
  font-family: "SCR", "NFR";
  padding-right: 10px;
  margin-left: 10px;
  text-decoration: none;
}
</style>
