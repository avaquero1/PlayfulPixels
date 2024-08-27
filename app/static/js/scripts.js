// /static/js/scripts.js

window.onload = function() {
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
};
