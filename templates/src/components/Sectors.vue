<template>
  <div class="sectors">
    <label for="sectors">Sectors: </label>
    <select name="sectors" id="sectors" multiple size="5">
      <option 
        v-bind:key="sector.id" 
        v-for="sector in sectors" 
        :value="sector.id"
        :selected="selected.indexOf(sector.id) >= 0"
        >
        {{ sector.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "Sectors",
  props: [
    'sectors', 
    'selected'
    ],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
