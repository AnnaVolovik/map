<template>
  <div class='header'>
    <nav>
      <ul>
        <li><a href="#">Main Page</a></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {

	data () {
		return {
			contactsOpen: false,
		}
	},

	methods: {
		showContact() {
			this.contactsOpen = !this.contactsOpen
		}
	}
}
</script>

<style scoped>
nav {
	background: #1F2733;
	color:#9da5b3; 
	width:100%;
	z-index: 100;
}
nav ul {
	list-style:none;
	padding:0;
	margin:0;
	text-align:end;
	font-size:85%;
}
nav li {
	display:inline-block;
	padding:1%;
}
nav a {
	text-decoration:none;
	color:#9da5b3;
}
nav a:hover {
	color:#3c7ac5;
}
</style>