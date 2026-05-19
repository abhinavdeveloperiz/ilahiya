
const images = [
    "static/images/banner1.JPG",
    "static/images/banner2.jpg",
    "static/images/banner3.jpg"
];

let index = 0;
const slideshow = document.getElementById("slideshow-bg");

setInterval(() => {
    index = (index + 1) % images.length;
    slideshow.style.opacity = 0;
    setTimeout(() => {
        slideshow.src = images[index];
        slideshow.style.opacity = 1;
    }, 1000); // Duration matches the transition
}, 5000); // Change image every 5 seconds
