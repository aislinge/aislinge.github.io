<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <div class="col" v-for="repo in repos" :key="repo.id">
        <div class="card h-100">
          <div class="card-header shining" alt="cover">
            {{ repo["name"] }}
          </div>
          <div class="card-body">
            <!-- <h5 class="card-title">{{ repo['name'] }}</h5> -->
            <p class="card-text">
              {{
                repo["description"] ? repo["description"] : "这个项目没有介绍"
              }}
            </p>
          </div>
          <div class="card-footer d-flex justify-content-between">
            <small class="text-muted">{{
              computedTime(repo["updated_at"])
            }}</small>
            <a
              class="btn btn-sm"
              v-show="!repo['has_pages']"
              :href="repo['html_url']"
              >仓库页面</a
            >
            <a
              class="btn btn-sm"
              v-show="repo['has_pages']"
              :href="repo['homepage']"
              >项目首页</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
const axios = require("axios");
const moment = require("moment");

moment.locale("zh_CN");

let today = moment();

export default {
  name: "Repo",
  data() {
    return {
      repos_api: "https://api.github.com/users/aislinge/repos",
      repos: [],
      heartColor: "red",
    };
  },
  methods: {
    // NOTE 获取项目列表
    getRepoInfoList() {
      axios.get(this.repos_api).then((response) => {
        console.log(response.data);
        this.repos = response.data;
      });
    },
    computedTime(time) {
      let seconds = today.diff(moment(time), "seconds");
      if (seconds < 60) {
        return seconds + "秒以前";
      }
      let minutes = today.diff(moment(time), "minutes");
      if (minutes < 60) {
        return minutes + "分钟以前";
      }
      let hours = today.diff(moment(time), "hours");
      if (hours < 12) {
        console.log(hours);
        return hours + "小时以前";
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
    computedCover(name) {
      // eslint-disable-next-line no-useless-escape
      let regex = /\W/g;
      name = name.replace(regex, " ");
      let holder = {
        img: "100x30",
        auto: "yes",
        theme: "github",
        size: 5,
        text: name,
      };
      return holder;
    },
  },
  mounted() {
    this.getRepoInfoList();
  },
};
</script>

<style scoped>
* {
  font-family: "SCR";
}
.card {
  box-shadow: 4px 4px 20px 5px rgba(0, 0, 0, 0.4);
  border-radius: 10px;
  background: black;
}
.card >>> .card-header {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  display: block;
}
div.row {
  margin-top: 20px;
}
.list-group-item {
  margin-top: 30px;
}
.card-body {
}
.card-text {
  color: #fff;
}
.card-footer {
  line-height: 30px;
}
.card-footer > .btn {
  color: #fff;
}
.card-footer > .text-muted {
  color: #fff;
}

.shining {
  /* font-size: 2em; */
  font-family: Lato, sans-serif;
  letter-spacing: 4px;
  text-transform: uppercase;
  background: linear-gradient(
    45deg,
    #5f86f2 0%,
    #a65ff2 10%,
    #f25fd0 30%,
    #f25f61 50%,
    #f2cb5f 60%,
    #abf25f 70%,
    #5ff281 80%,
    #5ff2f0 100%
  );
  background-size: 80%;
  background-repeat: no-repeat;
  color: transparent;
  background-clip: text;
  animation: shining 3s linear infinite;
}

@keyframes shining {
  from {
    background-position: -400% -400%;
  }
  to {
    background-position: 400% 400%;
  }
}
.btn {
  border: 1px solid #fff;
}
</style>
