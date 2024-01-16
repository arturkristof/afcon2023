<script setup lang="ts">
import { ref } from 'vue'
import db from "../db.json"
import LeaderBoard from "../components/LeaderBoard.vue"
import TheNextGame from "../components/TheNextGame.vue"

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
        <the-next-game :games="afconDb['games']"></the-next-game>
      </v-col>
      <v-col cols="12">
        <leader-board :results="afconDb['leaders']" :title="'Punkty'" :subtitle="'Suma punktów'"></leader-board>
      </v-col>
      <v-col cols="12">
        <leader-board :results="afconDb['snipers']" :title="'Snajperzy'" :subtitle="'Ilość trafionych wyników'"></leader-board>
      </v-col>
      <v-col cols="12">
        <leader-board :results="afconDb['pizda_streaks']" :title="'Pizda streak'" :subtitle="'Najdłuższy streak 0 punktów'"></leader-board>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped></style>
