<template>
  
  <div>
    <div id="frame">
      <div class="heart left"></div>
      <div class="heart right"></div>
      <div class="heart bottom"></div>
    </div>
    <div
      id="c"
      onclick='window.location.href="https://aislinge.github.io/OAO/";'
    >
      <H2></H2>
    </div>
    <div id="l">
      <H2></H2>
    </div>
    <div id="con">
      <h1>即使梦里梦见，醒来仍是贪心</h1>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>script>
export default {
  name: "Like",
};
<style>
body {
	overflow:hidden;
}
div {
	width:100px;
	height:100px;
	background:#E88D8D;
	position:absolute;
	top:50vh;
	left:50vw;
	margin-left:-50px;
	transform:rotate(45deg);
	border-radius:20px;
	transition:all ease  1s;
}
div::before {
	content:'';
	width:100px;
	height:100px;
	position:absolute;
	left:-38px;
	top:1px;
	border-radius:50%;
	background:#E88D8D;
	transition:all ease  1s;
}
div::after {
	content:'';
	width:100px;
	height:100px;
	position:absolute;
	right:-1px;
	top:-40px;
	border-radius:50%;
	background:#E88D8D;
	transition:all ease  1s;
}
.scla {
	transform:rotate(45deg) scale(20);
	box-shadow:11px 0px 30px 9px #E87777;
	opacity:0.4
}
/*		background:white}.scla::after {
	background:white
}
.scla::before {
	background:white;
}
*/
	h1 {
	opacity:0;
	position:absolute;
	top:50vh;
	left:50vw;
	margin-left:-100px;
	transition:all ease 1s;
	color:white;
	font-family:"Microsoft Yahei";
	font-weight:700;
	transform:translate(0px,-100px);
}
h1::before {
	content:'邝国强,';
	position:absolute;
	margin-top:-50px;
	margin-left:-10px;
}
.show {
	opacity:1;
	transform:translate(0,0);
}
.d2 {
	z-index:-1;
	opacity:0.2;
	animation:my 1s infinite linear;
}
@keyframes my {
	0% {
	transform:scale(1) rotate(45deg);
	opacity:1;
}
100% {
	transform:scale(1.65) rotate(45deg);
	opacity:0
}
}</style>
