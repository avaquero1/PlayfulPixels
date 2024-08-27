window.onload = function() {
    // Speech bubble functionality
    const speechBubble = document.getElementById('speechBubble');
    const messages = [
        "Welcome to PlayfulPixels!",
        "Ready to play?",
        "Let's have some fun!",
        "Choose a game to start!",
        "I'm Pixel, your guide!"
    ];

    let messageIndex = 0;

    // Function to change the speech bubble message
    function changeMessage() {
        speechBubble.innerText = messages[messageIndex];
        speechBubble.style.display = 'block'; // Show the bubble
        messageIndex = (messageIndex + 1) % messages.length; // Cycle through messages
    }

    // Initially show the speech bubble with a message
    changeMessage();

    // Change the message every 5 seconds
    setInterval(changeMessage, 5000);

    // Apply custom cursor functionality
    applyCustomCursors();

    // Observer to handle dynamically added clickable elements
    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            mutation.addedNodes.forEach(node => {
                if (node.nodeType === 1) { // Ensure it's an element node
                    const clickableElements = node.matches('a, button, .clickable') ? [node] : [];
                    const descendants = node.querySelectorAll ? Array.from(node.querySelectorAll('a, button, .clickable')) : [];
                    [...clickableElements, ...descendants].forEach(clickable => {
                        clickable.style.cursor = "url('/static/images/custom-pointer.png') 16 16, pointer";
                    });
                }
            });
        });
    });

    // Start observing the document for added nodes
    observer.observe(document.body, { childList: true, subtree: true });
};

// Function to apply the custom cursor to all clickable elements
function applyCustomCursors() {
    // Apply custom cursor globally
    document.body.style.cursor = "url('/static/images/custom-cursor.png') 16 16, default";

    // Apply custom pointer cursor to clickable elements
    document.querySelectorAll('a, button, .clickable').forEach(element => {
        element.style.cursor = "url('/static/images/custom-pointer.png') 16 16, pointer";
    });
}
