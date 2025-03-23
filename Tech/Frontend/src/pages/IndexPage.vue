<template>
  <!-- bg-image -->
  <q-page class="row items-center justify-evenly ">
    <example-component
      title="Example component"
      active
    ></example-component>
  </q-page>
</template>

<script setup lang="ts">
import ExampleComponent from 'components/ExampleComponent.vue';

</script>

<style lang="scss">
.bg-image {
    background-image: url(bg.jpg);
    background-repeat: no-repeat;
    background-size:auto;
    opacity: 0.5;
  }
</style>