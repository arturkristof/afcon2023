<script setup lang="ts">
import { ref } from 'vue'
import db from "../db.json"
import LeaderBoard from "../components/LeaderBoard.vue"

let afconDb = ref(db)
let pageTitle = ref("Wyniki")
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <span class="text-h2"> {{ pageTitle }} </span>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <leader-board :results="afconDb['leaders']" :title="'Punkty'" :subtitle="'Suma punktów'"></leader-board>
      </v-col>
      <v-col cols="12">
        <leader-board :results="afconDb['pizda_streaks']" :title="'Pizda streak'" :subtitle="'Najdłuższy streak 0 punktów'"></leader-board>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped></style>
