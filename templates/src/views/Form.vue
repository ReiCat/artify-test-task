<template>
  <form class="form" @submit.prevent="submitHandler">
    <Alert :alert="alert" @close="alert = null" />
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
import Alert from "../components/Alert.vue";
import axios from "axios";

export default {
  name: "Form",
  components: {
    Name,
    Sectors,
    Terms,
    SaveButton,
    Alert,
  },
  data() {
    return {
      name: "",
      sectors: [],
      selectedSectors: [],
      isAgreed: false,
      isDisabled: true,
      isSaved: false,
      alert: null,
    };
  },
  methods: {
    async getSectors() {
      try {
        let { data } = await axios.get("/sectors");
        this.sectors = data;
      } catch (e) {
        this.alert = {
          title: "Error",
          text: e.message,
        }
      }
    },
    async getUserData() {
      try {
        let { data } = await axios.get("/user");
        if (data !== undefined) {
          this.name = data.name;
          this.selectedSectors = data.selected_sectors;
          this.isAgreed = data.agreed_to_terms;
          this.onChange();
        }
      } catch (e) {
        this.alert = {
          title: "Error",
          text: e.message,
        }
      }
    },
    async submitHandler() {
      try {
        const name = document.getElementById("name").value;
        const selectedSectors = [
          ...document.getElementById("sectors").selectedOptions,
          ].map((sector) => sector.value);
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
        this.onChange();
      } catch (e) {
        this.alert = {
          title: "Error",
          text: e.message,
        }
      }
    },
    onChange() {
      if (this.name.length === 0 || this.selectedSectors.length === 0) {
        this.isDisabled = true;
      } else {
        this.isDisabled = false;
      }
    },
  },
  mounted() {
    this.getSectors();
    this.getUserData();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
