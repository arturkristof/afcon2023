<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{
  title: string,
  subtitle: string,
  results: Object[]
}>()

const rankedItems = computed(() => {
  let rawResults = [ ...props.results ]
  let lastVal = -1
  let lastRank = 0
  rawResults.forEach(entry => {
    if (entry.points != lastVal) {
      lastVal = entry.points
      lastRank += 1
    }
    entry['rank'] = lastRank
  })
  return rawResults
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
      <v-list :items="rankedItems" :item-title="item => `${item.rank}. ${item.name} - ${item.points}`" item-value="points">
      </v-list>
    </v-card-text>
  </v-card>
</template>