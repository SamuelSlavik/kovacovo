<script lang="ts" setup>

export type NotificationProps = {
  type?: string;
  primaryColor?: string;
  secondaryColor?: string;
  tertiaryColor?: string;
  position?: string;
};
const props = defineProps<NotificationProps>();

const {
  type = 'spinner',
  primaryColor = '#609966',
  secondaryColor = '#ffffff',
  tertiaryColor = '#ecf0f1',
  position = '',
} = props;

</script>

<template>
  <div class="loader-quark"></div>
</template>

<style>
.loader-quark {
  color: inherit;
  background-color: transparent;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}


/* --------------------------------- TYPES --------------------------------- */
.loader-quark {
  width: 2rem;
  padding: 0.3rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: v-bind(primaryColor);
  --_m:
      conic-gradient(transparent 10%, v-bind(primaryColor)),
      linear-gradient(v-bind(primaryColor) 0 0) content-box;
  -webkit-mask: var(--_m);
  mask: var(--_m);
  -webkit-mask-composite: source-out;
  mask-composite: subtract;
  animation: spinner 1s infinite linear;
}


/* ------------------------------ ANIMATIONS ------------------------------ */
@keyframes spinner {
  to {transform: rotate(1turn)}
}

</style>