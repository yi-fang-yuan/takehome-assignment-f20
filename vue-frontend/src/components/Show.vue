<template>
  <!-- PART 4: Add your code here -->
  <div class="book">
    <div class="column1">
      <p>{{name}}</p>
    </div>
    <div class="column1">
      <Counter :counter="episodes" />
    </div>
  </div>
</template>

<script>
import Counter from "./Counter.vue";
// PART 4: Add your code here
export default {
  props: ["id", "name", "episodes_seen"],
  data() {
    return {
      episodes: this.episodes_seen
    };
  },
  components: {
    Counter
  }
};
</script>

<style>
/* It says in the instruction to put the counter next to the name */
.book {
  display: flex;
  justify-content: center;
}
.column1{
  display:flex;
  flex-direction: column;
  justify-content: center;
  width:30%;
}
</style>
