<template>
  <div>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view />
  </div>
</template>
<style>
/* add some global class */
@font-face {
  font-family: lalezar;
  src: url(http://127.0.0.1:8000/static/font/Lalezar.ttf);
}
* {
  margin: 0;
  padding: 0;
  border: 0;
  font-family: "Lalezar", cursive;
  box-sizing: border-box;
  color: #ffffff;
}
html {
  font-size: 10px;
  font-family: lalezar;
}
body {
  background-color: rgb(13, 13, 13);
}
.container {
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  padding: 1rem 8%;
  max-width: 1300px;
}
img {
  width: 100%;
}
.card {
  box-shadow: 0.1rem 0.1rem 1rem 0.05rem rgb(112, 112, 112);
  border-radius: 3.5rem;
  background-color: white;
}
.txt {
  background-color: white;
  box-shadow: 0 0 0.5rem 0.1rem rgba(78, 78, 78, 0.5);
  padding: 0.5rem 1.5rem;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  direction: rtl;
  outline: none;
}
.btn {
  border-radius: 1rem;
  padding: 0.5rem 2rem;
  box-shadow: 0 0 0.5rem 0.1rem rgba(78, 78, 78, 0.5);
  background-color: #ae321f;
  color: #ffffe9;
  font-size: 2rem;
}
/* font-align */
.fa-c {
  text-align: center;
}
.fa-r {
  text-align: right;
}
.fa-l {
  text-align: left;
}
.fa-j {
  text-align: justify;
  direction: rtl;
}
</style>
