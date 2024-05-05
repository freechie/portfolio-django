document.addEventListener("DOMContentLoaded", function () {
	const menuToggle = document.getElementById("menu-toggle");
	const menuToggleContainer = document.getElementById("menu-toggle-container");
	const menu = document.getElementById("menu");
	const navLinks = document.querySelectorAll("#menu a");
	const scrollLeftButton = document.getElementById("scrollLeftButton");
	const scrollRightButton = document.getElementById("scrollRightButton");

	if (scrollLeftButton) {
		scrollLeftButton.addEventListener("click", scrollLeft);
	}

	if (scrollRightButton) {
		scrollRightButton.addEventListener("click", scrollRight);
	}

	// Function to open or close the menu with animation
	function toggleMenu(open) {
		if (open) {
			menu.classList.remove("hidden");
			setTimeout(() => {
				menu.style.opacity = 1;
				menu.style.height = "auto";
			}, 10);
		} else {
			menu.style.opacity = 0;
			menu.style.height = 0;
			setTimeout(() => {
				menu.classList.add("hidden");
			}, 300);
		}
	}

	// Adjusts the menu and hamburger icon based on the window size
	function adjustMenuForWindowSize() {
		if (window.innerWidth >= 1024) {
			// Window is wider than 1024px
			menuToggleContainer.style.opacity = 0; // Hide hamburger icon
			toggleMenu(true); // Show menu items without animation
		} else {
			// Window is less than 1024px
			menuToggleContainer.style.opacity = 1; // Show hamburger icon
			if (!menu.classList.contains("hidden")) {
				toggleMenu(false); // Hide menu items with animation
			}
		}
	}

	// Event listener for the hamburger menu toggle click event
	menuToggle.addEventListener("click", function () {
		const isOpen = menu.classList.contains("hidden");
		toggleMenu(isOpen);
	});

	// Event listeners for each link in the navigation menu to close the menu on click
	navLinks.forEach((link) => {
		link.addEventListener("click", () => {
			if (window.innerWidth < 1024) {
				toggleMenu(false); // Close menu
			}
		});
	});

	// Event listener for window resize events
	window.addEventListener("resize", adjustMenuForWindowSize);

	// Initial adjustment based on the current window size
	adjustMenuForWindowSize();
});

// Assuming the nonce is set on a meta tag with the name attribute set to 'csp-nonce'
const cspNonceMeta = document.querySelector('meta[name="csp-nonce"]');
if (cspNonceMeta) {
	window.CSP_NONCE = cspNonceMeta.content;
}

var swiper = new Swiper(".centered-slide-carousel", {
	centeredSlides: true,
	paginationClickable: true,
	loop: true,
	spaceBetween: 30,
	slideToClickedSlide: true,
	pagination: {
		el: ".centered-slide-carousel .swiper-pagination",
		clickable: true,
	},
	breakpoints: {
		1920: {
			slidesPerView: 4,
			spaceBetween: 30,
		},
		1028: {
			slidesPerView: 2,
			spaceBetween: 10,
		},
		990: {
			slidesPerView: 1,
			spaceBetween: 0,
		},
	},
});

function scrollLeft() {
	const container = document.querySelector(".carousel-container");
	container.scrollBy({ left: -300, behavior: "smooth" });
}

function scrollRight() {
	const container = document.querySelector(".carousel-container");
	container.scrollBy({ left: 300, behavior: "smooth" });
}
