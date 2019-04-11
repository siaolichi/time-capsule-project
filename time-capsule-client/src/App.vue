<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-inverse" style="padding: 20px;">
        <router-link style="padding: 20px;" to="/">Home</router-link>|
        <router-link style="padding: 20px;" to="/about">About</router-link>|
        <router-link style="padding: 20px;" to="/capsules">Capsules</router-link>
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
