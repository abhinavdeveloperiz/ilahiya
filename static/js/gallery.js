
// Get modal elements
const modal = document.getElementById('imageModal');
const enlargedImg = document.getElementById('enlargedImage');

// Add click event to all gallery images
document.querySelectorAll('.gallery-image').forEach(image => {
    image.addEventListener('click', () => {
        modal.style.display = 'flex';
        enlargedImg.src = image.src;
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    });
});

// Close modal when clicking outside image
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

// Close modal with ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.style.display === 'flex') {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});
