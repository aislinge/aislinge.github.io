<template>
  <div id="logo">
    <i class="nf nf-fa-heart"></i>
    <span class="c">
      <router-link to="/NIXIAK">C</router-link>
    </span>
  </div>
</template>

<script>
export default {
  name: "CustomLogo",
  data() {
    return {
      heartColor: "red",
      circleColor: "black",
    };
  },
};
</script>

<style scoped>
#logo {
}
#logo .nf.nf-fa-heart {
  color: red;
  font-size: 200px;
  position: relative;
}
.c {
  position: absolute;
  left: 50%;
  line-height: 200px;
}
.c > a {
  text-decoration: none;
  color: black;
}
</style>