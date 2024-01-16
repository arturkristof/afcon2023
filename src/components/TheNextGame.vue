<script setup lang="ts">
import { computed } from 'vue'
import moment from 'moment'

const props = defineProps<{
  games: Object[],
}>()

const nextGames = computed(() => props.games.filter(game => {
  let gameDate = moment(game.Date)
  let now = moment()
  return gameDate.add(2, 'hours') > now
}))
const nextGame = computed(() => nextGames.value[0])
const names = ['Kwiatek', 'Filip', 'Komar', 'Artur', 'Mati', 'Plech', 'Lesiu', 'Komar jr']
const items = computed(() => {
  let res = []
  names.forEach(name => {
    res.push({
      name,
      home: nextGame.value[`${name} Home`],
      away: nextGame.value[`${name} Away`],
    })
  })
  return res
})
const headers = computed(() => [
  {title: '', value: 'name'},
  {title: nextGame.value['Home Team'], value: 'home', align: 'end'},
  {title: nextGame.value['Away Team'], value: 'away'},
])
</script>
<template>
  <v-card class="mx-auto my-8" elevation="16">
    <v-card-item>
      <v-card-subtitle>
        {{ 'Next game \n' }}
      </v-card-subtitle>
      <v-card-title>
        {{ `${nextGame['Home Team']} - ${nextGame['Away Team']}` }}
      </v-card-title>
      <v-card-subtitle>
        {{ moment(nextGame['Date']).format('DD.MM HH:mm') }}
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
      <v-data-table :items="items" :headers="headers" density="compact">
        <template #bottom></template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>