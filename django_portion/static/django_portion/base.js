document.addEventListener("DOMContentLoaded", function () {
	const menuToggle = document.getElementById("menu-toggle");
	const menuToggleContainer = document.getElementById("menu-toggle-container");
	const menu = document.getElementById("menu");
	const navLinks = document.querySelectorAll("#menu a");
	const scrollLeftButton = document.getElementById("scrollLeftButton");
	const scrollRightButton = document.getElementById("scrollRightButton");
	const emojiLink = document.querySelector(".emoji-link");

	if (emojiLink) {
		setTimeout(() => {
			emojiLink.classList.remove("hidden"); // Trigger emoji link transition
		}, 100);
	}

	function addScrollEvent(button, handler) {
		if (button) {
			button.addEventListener("click", handler);
		}
	}

	addScrollEvent(scrollLeftButton, scrollLeft);
	addScrollEvent(scrollRightButton, scrollRight);

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

	function adjustMenuForWindowSize() {
		if (window.innerWidth >= 1024) {
			menuToggleContainer.style.opacity = 0;
			toggleMenu(true);
		} else {
			menuToggleContainer.style.opacity = 1;
			if (!menu.classList.contains("hidden")) {
				toggleMenu(false);
			}
		}
	}

	menuToggle.addEventListener("click", () =>
		toggleMenu(menu.classList.contains("hidden"))
	);

	navLinks.forEach((link) => {
		link.addEventListener("click", () => {
			if (window.innerWidth < 1024) {
				toggleMenu(false);
			}
		});
	});

	window.addEventListener("resize", adjustMenuForWindowSize);
	adjustMenuForWindowSize();
});

const cspNonceMeta = document.querySelector('meta[name="csp-nonce"]');
if (cspNonceMeta) {
	window.CSP_NONCE = cspNonceMeta.content;
}

const swiper = new Swiper(".centered-slide-carousel", {
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
