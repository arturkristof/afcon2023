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
      home: nextGame.value[`${name} Home`],
      away: nextGame.value[`${name} Away`],
    })
  })
  return res
})

import type { VDataTable } from 'vuetify/components'

type ReadonlyHeaders = VDataTable['headers']
type UnwrapReadonlyArrayType<A> = A extends Readonly<Array<infer I>> ? I : never;
type ReadonlyDataTableHeader = UnwrapReadonlyArrayType<ReadonlyHeaders>;

type DeepMutable<T> = { -readonly [P in keyof T]: DeepMutable<T[P]> }
type DataTableHeader = DeepMutable<ReadonlyDataTableHeader>;
// @ts-expect-error
const headers: DataTableHeader[] = computed(() => {
  return [
    { title: '', value: 'name', align: 'start' },
    { title: nextGame.value['Home Team'], value: 'home', align: 'end' },
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
        <template #bottom></template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>