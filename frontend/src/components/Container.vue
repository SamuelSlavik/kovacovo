<script setup lang="ts">
import {ref} from "vue";

export type ContainerProps = {
  global?: boolean
}
const props = defineProps<ContainerProps>()

console.log(props.global)

</script>

<template>
  <div class="container" :class="props.global ? 'container--global' : ''">
    <slot />
  </div>
</template>

<style>
.container {
  width: 100%;
  max-width: var(--breakpoint);
  margin: 0 auto;
  padding: 1rem 1rem;
  font-weight: normal;
  position: relative;
}
.container--global {
  min-height: 100vh;
  padding-top: 5rem;
}
</style>
