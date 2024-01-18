<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{
  title: string,
  subtitle: string,
  results: any[]
}>()

const items = computed(() => {
  let lastVal = -1
  let lastRank = 0
  let rawResults: any[] = []

  props.results.forEach(entry => {
    if (entry.points != lastVal) {
      lastVal = entry.points
      lastRank += 1
    }
    rawResults.push({
      ...entry,
      rank: lastRank
    })
  })
  return rawResults
})

const headers = computed(() => {
  return [
    { title: 'Rank', value: 'rank', align: 'end' },
    { title: 'Name', value: 'name', align: 'start' },
    { title: 'Value', value: 'points', align: 'start' }
  ]
})


</script>
<template>
  <v-card class="mx-auto my-8" elevation="16">
    <v-card-item>
      <v-card-title>
        {{ props.title }}
      </v-card-title>
      <v-card-subtitle>
        {{ props.subtitle }}
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

<style scoped>
:deep(tbody tr):hover{
  background-color: #CFCFCF !important;
}
</style>