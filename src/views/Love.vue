<template>
  <div>
    <div id="frame">
      <div class="heart left"></div>
      <div class="heart right"></div>
      <div class="heart bottom"></div>
    </div>
    <div id="c" onclick='window.location.href="https://aislinge.github.io/OAO/";'>
     
    </div>
    <div id="l">
      
    </div>
    <div id="con">
      <h1>全天下好东西都该属于我，包括你在内</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Love",
};
</script>

<style scoped>
#frame {
  position: relative;
  width: 400px;
  height: 300px;
  margin: 100px auto;
}
.left,
.right {
  top: 0;
  width: 200px;
  height: 200px;
  border-radius: 50%;
}
.left {
  left: 35px;
}
.right {
  right: 35px;
  z-index: -1;
}
.bottom {
  bottom: 36px;
  left: 100px;
  width: 200px;
  height: 200px;
  transform: rotate(45deg);
  z-index: -1;
}
.heart {
  position: absolute;
  box-shadow: 0 0 40px #d5093c;
  animation: beat 0.8s ease infinite normal;
  background: linear-gradient(-90deg, #f50a45 0%, #d5093c 40%);
}
@keyframes beat {
  0% {
    transform: scale(1) rotate(225deg);
    box-shadow: 0 0 40px #d5093c;
  }
  50% {
    transform: scale(1.1) rotate(225deg);
    box-shadow: 0 0 70px #d5093c;
  }
  100% {
    transform: scale(1) rotate(225deg);
    box-shadow: 0 0 40px #d5093c;
  }
}
@keyframes a {
  0% {
    transform: scale(1) rotate(0deg);
  }
  50% {
    transform: scale(1.1) rotate(0deg);
  }
  100% {
    transform: scale(1) rotate(0deg);
  }
}
#c {
  /*right: 60%;left: 40%;*/
  margin: -15% 30%;
  position: absolute;
  animation: a 0.8s ease infinite normal;
}
#l {
  margin: -15% 67%;
  position: absolute;
  animation: a 0.8s ease infinite normal;
}
#con {
  margin-top: 30px;
  margin-bottom: 100px;
  text-align: center;
}
h1,
h2 {
  font-family: "YRDM";
}
</style>
