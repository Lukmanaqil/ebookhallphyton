@extends('layouts.app')

<style>
	body,
	h1,
	h2,
	h3,
	h4,
	h5,
	h6 {
		font-family: "Lato", sans-serif;
	}

	body,
	html {
		height: 100%;
		color: #777;
		line-height: 1.8;
	}

	/* Create a Parallax Effect */
	.bgimg-1,
	.bgimg-2,
	.bgimg-3 {
		background-attachment: fixed;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
	}

	/* First image (Logo. Full height) */
	.bgimg-1 {
		background-image: url('/miscImages/library-wallpaper-20.jpg');
		min-height: 100%;
	}

	.w3-wide {
		letter-spacing: 10px;
	}

	.w3-hover-opacity {
		cursor: pointer;
	}

	/* Turn off parallax scrolling for tablets and phones */
	@media only screen and (max-device-width: 1600px) {

		.bgimg-1,
		.bgimg-2,
		.bgimg-3 {
			background-attachment: scroll;
			min-height: 400px;
		}
	}
</style>


<body>
@section('content')
	<div style="background-color: rgb(168, 208, 230);">
		<!-- First Parallax Image with Logo Text -->
		<div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
			<div class="w3-display-middle" style="white-space:nowrap;">
				<span class="w3-center w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity"><span class="w3-hide-small"><a href="/book">E-BOOKHALL</a></span></span>
			</div>
		</div>

		<!-- Container (About Section) -->
		<div class="w3-content w3-container w3-padding-64" id="about">
			<h3 class="w3-center">ABOUT US</h3>
			<p>E-BookHall provides a platform for users to indulge through literature with famous authors.
				The main target of user classes are people who are avid readers that do not want to carry heavy books with them at all times.
				This application aims to encourage the consumption of information via digital access documents, like E-Books,
				PDFs, and e-news for a more environmentally-friendly paperless-mass-media. Apart from that, the managers will
				have access to the manage book function that allows them to add or remove books for the database.</p>

		</div>
	</div>
	

	<script>
		// Modal Image Gallery
		function onClick(element) {
			document.getElementById("img01").src = element.src;
			document.getElementById("modal01").style.display = "block";
			var captionText = document.getElementById("caption");
			captionText.innerHTML = element.alt;
		}


		// Used to toggle the menu on small screens when clicking on the menu button
		function toggleFunction() {
			var x = document.getElementById("navDemo");
			if (x.className.indexOf("w3-show") == -1) {
				x.className += " w3-show";
			} else {
				x.className = x.className.replace(" w3-show", "");
			}
		}
	</script>
@endsection
</body>
