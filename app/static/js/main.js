var socket = io();

document.addEventListener('DOMContentLoaded', function() {
    socket.on('response', function(data) {
        hideLoadingIndicator();
        addMessage(data.data, 'bot');
    });

    document.getElementById('sendButton').addEventListener('click', function() {
        sendMessage();
        showLoadingIndicator();
    });
});

function sendMessage() {
    var userInput = document.getElementById('userInput').value;
    addMessage(userInput, 'user');
    socket.emit('message', { data: userInput });
    document.getElementById('userInput').value = '';
}

function addMessage(message, sender) {
    var messages = document.getElementById('messages');
    var li = document.createElement('li');
    var messageClass = sender === 'user' ? 'user-message' : 'bot-message';
    
    li.classList.add(messageClass);
    var messageBubble = document.createElement('div');
    messageBubble.classList.add('message-bubble');
    messageBubble.textContent = message;
    li.appendChild(messageBubble);
    messages.appendChild(li);
}

function showLoadingIndicator() {
    document.getElementById('loadingIndicator').classList.remove('d-none');
}

function hideLoadingIndicator() {
    document.getElementById('loadingIndicator').classList.add('d-none');
}
