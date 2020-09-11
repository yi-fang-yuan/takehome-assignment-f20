<template>
  <div>
    <p>I'm a Counter!</p>
    <div v-if="counter != null">
      <button v-on:click="episodes_seen += 1">Add 1</button>
      <button v-on:click="episodes_seen -= 1">Minus 1</button>
      <p>{{episodes_seen}}</p>
    </div>
    <div v-else>
      <button v-on:click="count += 1">Add 1</button>
      <button v-on:click="count -= 1">Minus 1</button>
      <p>{{this.count}}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['counter'],
  data() {
    return {
      count: 0,
      episodes_seen: this.counter

    };
  }
};
</script>

<style>
</style>

