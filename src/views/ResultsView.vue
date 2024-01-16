<script setup lang="ts">
import { ref } from 'vue'
import db from "../db.json"

let afconDb = ref(db)
</script>

<template>
  <v-app>
    <v-main>
      <span> Testing </span>
      {{ afconDb['leaders'] }}
    </v-main>
  </v-app>
</template>

<style scoped></style>
