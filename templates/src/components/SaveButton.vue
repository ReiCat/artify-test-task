<template>
  <div class="save">
    <input type="submit" value="Save" :disabled="isDisabled" />
    <span v-if="isSaved"> Saved</span>
  </div>
</template>

<script>
export default {
  name: "SaveButton",
  props: {
    isDisabled: Boolean,
    isSaved: Boolean,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
