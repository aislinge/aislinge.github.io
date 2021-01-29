<template>
  <div>
    <div class="main-bg"></div>
    <vue-baberrage
      :isShow="barrageIsShow"
      :barrageList="barrageList"
      :throttleGap="throttleGap"
      :lanesCount="lanesCount"
      :messageHeight="messageHeight"
      class="baberrage"
    >
      <template v-slot:default="slotProps">
        <span
          class="badge rounded-pill"
          :class="slotProps.item.color"
          style="background: none; font-family: 'YRDM'"
          :style="slotProps.item.size + slotProps.item.color"
        >
          {{ slotProps.item.msg }}
        </span>
      </template>
    </vue-baberrage>

    <div class="main">
      <CustomLogo class="logo" />
    </div>
  </div>
</template>

<script>
import CustomLogo from "@/components/CustomLogo";
import { MESSAGE_TYPE } from "vue-baberrage";
const moment = require("moment");
const axios = require("axios");

moment.locale("zh-cn");
let start_time = moment("20201105");
var now_time = moment();

let url =
  "https://api.lovelive.tools/api/SweetNothings/15/Serialization/Json?genderType=M";

export default {
  name: "Home",
  components: {
    CustomLogo,
  },
  data() {
    return {
      start_time,
      now_time,
      msg: "",
      days: now_time.diff(start_time, "days"),
      throttleGap: 2000,
      lanesCount: 16,
      messageHeight: 35,
      barrageIsShow: true,
      currentId: 0,
      barrageLoop: true,
      // TODO 这里的弹幕内容应该为日记内容摘选
      barrageList: [],
    };
  },
  methods: {
    addToList() {
      axios.get(url).then((response) => {
        for (let index = 0; index < 15; index++) {
          let tmp_size = Math.random();
          this.barrageList.push({
            id: ++this.currentId,
            msg: response.data["returnObj"][index],
            time: Math.random() * 10 + 10,
            color:
              "color: rgba(" + 0 + "," + 0 + "," + 0 + "," + tmp_size + ");",
            size: "font-size: " + Math.ceil(tmp_size * 2.5) + 2 + "px;",
            type: MESSAGE_TYPE.NORMAL,
          });
        }
      });
    },
  },
  mounted() {
    let that = this;
    that.addToList();
    setInterval(function () {
      that.addToList();
    }, 10000);
  },
};
</script>

<style scoped>
.main {
  padding-top: 150px;
  text-align: center;
  text-align: center;
  position: relative;
  height: 650px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 10%);
  overflow: hidden;
}
.main > h1 {
  margin-top: 50px;
  font-family: "NFM", "SCR";
}
.baberrage-stage {
  height: 700px;
  overflow: hidden;
}
.logo {
  font-size: 120px;
}
</style>
