<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <v-app class="white">
    <v-main>
      <router-view> </router-view>
    </v-main>
  </v-app>
</template>

<style>
body {
  background-color: #FFFFFF !important
  ;
}
</style>
