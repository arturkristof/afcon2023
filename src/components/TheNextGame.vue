<script setup lang="ts">
import { computed } from 'vue'
import moment from 'moment'

const props = defineProps<{
  games: any[],
}>()

const nextGames = computed(() => props.games.filter(game => {
  let gameDate = moment(game.Date)
  let now = moment()
  return gameDate.add(2, 'hours') > now
}))
const nextGame = computed(() => nextGames.value[0])
const names = ['Kwiatek', 'Filip', 'Komar', 'Artur', 'Mati', 'Plech', 'Lesiu', 'Komar jr']
const items = computed(() => {
  let res: any[] = []
  names.forEach(name => {
    res.push({
      name,
      picture: `${name}.jpg`,
      home: nextGame.value[`${name} Home`],
      colon: ':',
      away: nextGame.value[`${name} Away`],
    })
  })
  return res
})

const headers = computed(() => {
  return [
    { title: '', value: 'picture', align: 'end' },
    { title: '', value: 'name', align: 'end' },
    { title: nextGame.value['Home Team'], value: 'home', align: 'end' },
    { title: '-', value: 'colon', align: 'end', width: '10px' },
    { title: nextGame.value['Away Team'], value: 'away', align: 'start' },
  ]
})
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
      <!-- @vue-ignore -->
      <v-data-table :items="items" :headers="headers" density="compact">
        <template v-slot:item.picture="{ value }">
          <v-avatar :image="value" :size="30"></v-avatar>
        </template>
        <template #bottom></template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<style scoped>
:deep(td):nth-child(n+2){
  padding-left: 4px !important;
  padding-right: 4px !important;
}
:deep(th):nth-child(n+2){
  padding-left: 4px !important;
  padding-right: 4px !important;
}
:deep(tbody tr):hover{
  background-color: #CFCFCF !important;
}
</style>