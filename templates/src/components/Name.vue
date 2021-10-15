<template>
  <div class="name">
    <label for="name">Name: </label>
    <input 
      id="name"
      type="text" 
      :value="modelValue"
      @input="onChange"
    />
  </div>
</template>

<script>
export default {
  name: "Name",
  emits: ['update:modelValue'],
  props: {
    modelValue: String,
  },
  methods: {
    onChange(event) {
      this.$emit('update:modelValue', event.target.value);
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
