<template>
  <div class="capsule1">
    <input
      class="form-control form-control-lg"
      type="text"
      placeholder="talk with me here"
      v-model="chat.user_sentence"
      @keyup.enter="requestResponse"
    >
    <h3>{{chat.user_sentence}}</h3>
    <h1>{{response}}</h1>
  </div>
</template>
<script>
export default {
  name: "capsule1",
  data() {
    return {
      chat: {
        sentence: "hi",
        responsed: ""
      }
    };
  },
  methods: {
    requestResponse() {
      const vm = this;
      console.log("got!");

      this.axios
        .post(process.env.VUE_APP_API_URI, {
          sentence: this.chat.sentence
        })
        .then(response => {
          console.log(response.data);
        });
    }
  }
};
</script>
<style scoped>
.capsule1 {
  width: 60%;
  margin: auto;
}
.form-control {
  size: 3em;
  height: 3em;
  width: 50%;
  margin: auto;
}
</style>
