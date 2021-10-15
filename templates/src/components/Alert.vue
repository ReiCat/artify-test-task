<template>
  <div v-if="alert">
    <h3>{{ alert.title }}</h3>
    <p>{{ alert.text }}</p>
    <button @click="$emit('close')">Close</button>
  </div>
</template>

<script>
export default {
    name: "Alert",
    emits: ['close'],
    props: ['alert']

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>