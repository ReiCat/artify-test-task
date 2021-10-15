<template>
  <div class="terms">
    <input
     id="terms"
     type="checkbox"
     :checked="isAgreed"
    />
    <label for="terms"> Agree to terms</label>
  </div>
</template>

<script>
export default {
  name: "Terms",
  props: {
    isAgreed: Boolean,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
