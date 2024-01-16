<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <v-app>
    <v-main>
      <span>Testing app</span>
      <router-view> </router-view>
    </v-main>
  </v-app>
</template>

<style scoped></style>
