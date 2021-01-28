<template>
  <div class="container">
    <hr />
    <div class="d-flex justify-content-between bd-highlight mb-3">
      <span class="badge colorful">
        <a
          href="mailto:alkaid.yu@gmail.com"
          class="text-reset text-decoration-none light"
          >{{ author_mail }}</a
        >
      </span>
      <span class="badge colorful">{{ slogan }}</span>
      <span class="badge colorful">版本：{{ version }}</span>
    </div>
  </div>
</template>
<script>
var moment = require("moment");

moment.locale("zh-cn");

export default {
  name: "Footer",
  data() {
    return {
      version: "1.0.0",
      seconds: "",
      slogan: "可以微弱，但要有光",
      author_mail: "alkaid.yu@gmail.com",
    };
  },
  methods: {},
};
</script>
<style scoped>
.container {
  margin-top: 30px;
}
.badge {
  font-family: "NFM", "SCR";
  background: #fdd;
  color: #2d2e2e;
}
</style>