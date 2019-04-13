<template>
  <div class="capsule1">
    <p id="respond">{{chat.respond}}</p>
    <div id="sound-box"></div>
    <input
      class="form-control form-control-lg"
      type="text"
      placeholder="talk with me here"
      v-model="chat.user_sentence"
      @keyup.enter="requestResponse()"
    >
  </div>
</template>
<script>
import jQuery from "jquery";
const $ = jQuery;
export default {
  name: "capsule1",
  data() {
    return {
      chat: {
        user_sentence: "",
        respond: ""
      }
    };
  },
  mounted() {
    let input_text = "Hello, My name is Li-Chi. Today is July 9th 2018";
    this.getSoundResponse(input_text);
  },

  methods: {
    getSoundResponse(data) {
      this.axios
        .post(process.env.VUE_APP_API_URI + "/sound", {
          generate_sound: data
        })
        .then(response => {
          $("#sound-box").html(response.data);
          console.log(response);
        })
        .catch(err => console.log(err));
    },

    requestResponse() {
      const vm = this;
      console.log("got!");

      this.axios
        .post(process.env.VUE_APP_API_URI + "/response", {
          user_sentence: this.chat.user_sentence
        })
        .then(response => {
          console.log(response.data);
          vm.chat.respond = response.data["response"];
          this.getSoundResponse(response.data["response"]);
        });
    }
  }
};
</script>
<style scoped>
.capsule1 {
  width: 80%;
  height: 80vh;
  margin: auto;
}
.form-control {
  top: 90vh;
  left: 20%;
  position: fixed;
  text-align: left;
  size: 3em;
  height: 3em;
  width: 60%;
  margin: auto;
}
#respond {
  font-family: chogokubosogothic;
  font-size: 120px;
  text-align: left;
}
</style>
