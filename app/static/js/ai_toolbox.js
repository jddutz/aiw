// app/static/js/ai_toolbox.js

// Floating Action Button + Context Menu
document.getElementById('aiToolboxButton').addEventListener('click', function () {
    var fab = document.getElementById('aiToolboxButton');
    var contextMenu = document.getElementById('aiContextMenu');

    if (contextMenu.style.display === 'none' || contextMenu.style.display === '') {
        contextMenu.style.display = 'block';
        fab.classList.add('fab-active');
    } else {
        contextMenu.style.display = 'none';
        fab.classList.remove('fab-active');
    }
});

// Common toolbox functions

/**
 * Make an AJAX POST request.
 *
 * @param {string} url - The URL to send the request.
 * @param {Object} data - The data to send as JSON.
 * @param {Function} successCallback - Function to execute on a successful response.
 * @param {Function} errorCallback - Function to execute on a failed response.
 */
function ajaxPost(url, data, successCallback, errorCallback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                successCallback(response);
            } else {
                errorCallback(xhr);
            }
        }
    };
    xhr.send(JSON.stringify(data));
}

/**
 * Display an AI-generated message in an alert.
 *
 * @param {Object} aiResponse - The AI's response object.
 */
function displayAIResponse(aiResponse) {
    alert(aiResponse.content);
}

/**
 * Toolbox function displays an alert with an AI greeting.
 */
function say_hello() {
    var messageData = {
        content: "Hello, AI! Can you greet our user?"
    };

    ajaxPost(
        '/api/v1/chat/',
        messageData,
        function (response) { // Success callback
            displayAIResponse(response);
        },
        function (error) { // Error callback
            console.error('Error:', error);
            alert('Sorry, something went wrong.');
        }
    );
}

function help_chat() {
    // This can be updated similarly when you implement the chat feature
    alert('Help chat');
}