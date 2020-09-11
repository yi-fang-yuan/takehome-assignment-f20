<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions v-bind:complete="true" />
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <div class="show">
      <form @submit="addShow">
        <input v-model="new_show" palceholder="add a show" />
        <button type="submit">Add new Show</button>
      </form>
      <Show
        v-for="show in shows"
        :key="show.id"
        :id="show.id"
        :name="show.name"
        :episodes_seen="show.episodes_seen"
      />
    </div>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  methods:{
    addShow: function(e){
      e.preventDefault();
      this.shows.push({
        id : this.new_id,
        name: this.new_show,
        episodes_seen : 0
      })
      this.new_id += 1
    }
  },
  data() {
    return {
      new_id: 4,
      new_show: "",
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  }
};
</script>

<style>
.show {
  height: 100%;
}
</style>


