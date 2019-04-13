<template>
  <div class="caption">
    <h1>Working on ...</h1>
    <!-- <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p> -->
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  created() {
    console.log(this.$route.params.id);
  }
};
</script>