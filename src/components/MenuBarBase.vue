<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <div class="container">
      <!-- NOTE LOGO -->
      <router-link class="navbar-brand" to="/home">
        <slot name="nav_logo">
          
          <i class="nf nf-fae-carot"></i>
         
        </slot>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/blog">文 章</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/repo">项 目</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/about"
              >关 于</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "MemuBarBase",
};
</script>

<style scoped>
.navbar-brand {
  letter-spacing: 9px;
}
.nf.nf-fae-carot {
  color: #ed9121;
  font-size: 35px;
}
.navbar-brand,
.nav-item {
  padding-right: 20px;
}
.navbar-nav a.nav-link {
  color: #000;
}
.navbar-nav a.nav-link.active {
  color: #f00;
}
</style>

