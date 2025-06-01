// This file contains additional JavaScript functionality for the application

document.addEventListener('DOMContentLoaded', function() {
    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        const dropdowns = document.querySelectorAll('.dropdown-content');
        dropdowns.forEach(dropdown => {
            if (!dropdown.parentElement.contains(e.target)) {
                dropdown.classList.add('hidden');
            }
        });
    });

    // Show loading spinner when download starts
    const downloadButtons = document.querySelectorAll('.download-video-btn');
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Create loading overlay
            const loadingOverlay = document.createElement('div');
            loadingOverlay.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
            loadingOverlay.innerHTML = `
                <div class="bg-darker-bg p-6 rounded-lg shadow-lg text-center">
                    <div class="loader h-12 w-12 rounded-full border-4 border-gray-600 mx-auto"></div>
                    <p class="mt-4 text-xl">Starting download...</p>
                    <p class="text-secondary-text mt-2">This may take a moment</p>
                </div>
            `;
            
            document.body.appendChild(loadingOverlay);
            
            // Remove loading overlay after 3 seconds
            // In a real app, this would be handled by tracking the actual download progress
            setTimeout(() => {
                document.body.removeChild(loadingOverlay);
            }, 3000);
        });
    });
});

// Function to toggle mobile menu
function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
}

// Function to copy video link to clipboard
function copyVideoLink(url) {
    navigator.clipboard.writeText(url).then(() => {
        // Show success notification
        const notification = document.createElement('div');
        notification.className = 'fixed bottom-4 right-4 bg-green-600 text-white px-4 py-2 rounded-lg shadow-lg';
        notification.innerText = 'Link copied to clipboard!';
        document.body.appendChild(notification);
        
        // Remove notification after 2 seconds
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 2000);
    });
}