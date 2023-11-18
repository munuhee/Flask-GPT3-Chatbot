var socket = io();

socket.on('response', function(data) {
    addMessage(data.data, 'bot');
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
    li.textContent = sender + ': ' + message;
    messages.appendChild(li);
}
