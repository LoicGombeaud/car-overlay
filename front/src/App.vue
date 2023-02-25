<script>
import "./scss/styles.scss"
</script>

<template>
  <div class="container">
    <div class="row px-2">
      <div class="col-lg-3"></div>
      <div class="col-lg-6">
        <div class="display-5 my-3">Le point de vue de l'automobiliste</div>
          <router-view />
      </div>
      <div class="col-lg-3"></div>
    </div>
  </div>
</template>
