<template>
  <form class="form" @submit.prevent="submitHandler">
    <Name v-model="name" @input="onChange" />
    <Sectors :sectors="sectors" :selected="selectedSectors" @input="onChange" />
    <Terms :isAgreed="isAgreed" />
    <SaveButton :isDisabled="isDisabled" :isSaved="isSaved" @input="onChange" />
  </form>
</template>

<script>
import Name from "../components/Name.vue";
import Sectors from "../components/Sectors.vue";
import Terms from "../components/Terms.vue";
import SaveButton from "../components/SaveButton.vue";
import axios from "axios";

export default {
  name: "Form",
  components: {
    Name,
    Sectors,
    Terms,
    SaveButton,
  },
  data() {
    return {
      name: "",
      sectors: [],
      selectedSectors: [],
      isAgreed: false,
      isDisabled: true,
      isSaved: false,
    };
  },
  methods: {
    async getSectors() {
      let { data } = await axios.get("/sectors");
      this.sectors = data;
    },
    async getUserData() {
      let { data } = await axios.get("/user");
      if (data !== undefined) {
        this.name = data.name;
        this.selectedSectors = data.selected_sectors;
        this.isAgreed = data.agreed_to_terms;
        this.onChange()
      }
    },
    async submitHandler() {
      const name = document.getElementById("name").value;
      const selectedSectors = [...document.getElementById("sectors").selectedOptions].map(sector => sector.value);
      const isAgreed = document.getElementById("terms").checked;
      const { data } = await axios.post("/user", {
        name: name,
        selectedSectors: selectedSectors,
        isAgreed: isAgreed,
      });
      this.name = data.name;
      this.selectedSectors = data.selected_sectors;
      this.isAgreed = data.agreed_to_terms;
      this.isSaved = true;
      this.onChange()
    },
    onChange() {
      if (this.name.length === 0 || this.selectedSectors.length === 0) {
        this.isDisabled = true
      } else {
        this.isDisabled = false
      }
    }
  },
  mounted() {
    this.getSectors();
    this.getUserData();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
