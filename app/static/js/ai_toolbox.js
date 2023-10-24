// app/static/js/ai_toolbox.js

// Find the div with id = 'aiw-content'
let aiwContentDiv = document.getElementById('aiw-content');
if (!aiwContentDiv) help_context_id = null; else help_context_id = aiwContentDiv.getAttribute('data-help-context-id');

var currentConversationId = null;

var chatMessageContainer = document.getElementById('chatMessageContainer');

/**
 * Toggles display of the context menu and floating action button
 */
function toggleContextMenu() {
    var fab = document.getElementById('aiToolboxButton');
    var contextMenu = document.getElementById('aiContextMenu');

    if (contextMenu.style.display === 'none' || contextMenu.style.display === '') {
        contextMenu.style.display = 'block';
        fab.classList.add('fab-active');
    } else {
        contextMenu.style.display = 'none';
        fab.classList.remove('fab-active');
    }
}

/**
 * Opens the chat interface and hides the context menu.
 */
function openChatInterface() {
    var chatInterface = document.getElementById('chatInterface');
    var contextMenu = document.getElementById('aiContextMenu');

    chatInterface.style.display = 'block';
    contextMenu.style.display = 'none';
}

/**
 * Closes the chat interface and shows the context menu if showContextMenu is true.
 */
function closeChatInterface(showContextMenu) {
    var chatInterface = document.getElementById('chatInterface');
    var contextMenu = document.getElementById('aiContextMenu');

    chatInterface.style.display = 'none';

    if (showContextMenu) {
        contextMenu.style.display = 'block';
    }
}

/**
 *  Renders a single chat message to the chat interface.
 */
function appendChatMessage(message) {
    var newMessageDiv = document.createElement('div');

    newMessageDiv.className = "chat_message_" + message.role.toLowerCase();
    newMessageDiv.innerText = message.content;

    chatMessageContainer.appendChild(newMessageDiv);
}

/**
 * Renders chat messages to the chat interface.
 */
function renderChatMessages(messages) {
    // Clear the chat messages container
    chatMessageContainer.innerHTML = '';

    for (let i = 0; i < messages.length; i++) {
        appendChatMessage(messages[i]);
    }

    chatMessageContainer.scrollTop = chatMessageContainer.scrollHeight;
}

/**
 * Extract the contents of the current page and return it as plain text
 * for use as context in REST API calls.
 */
function loadPageContent() {
    if (!aiwContentDiv) return '';

    let textValues = [];

    function extractTextFromNode(node) {
        if (node.nodeType === Node.TEXT_NODE && node.nodeValue.trim() !== "") {
            // If the current node is a text node and not empty, push its value to the list
            textValues.push(node.nodeValue.trim());
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            // If the current node is an element node
            if (node.tagName.toLowerCase() === 'textarea' || (node.tagName.toLowerCase() === 'input' && ['text', 'number', 'password', 'email', 'search'].includes(node.type))) {
                // If the element is a textarea or specific type of input, push its value
                textValues.push(node.value);
            } else {
                // Otherwise, loop through its children recursively
                for (let child of node.childNodes) {
                    extractTextFromNode(child);
                }
            }
        }
    }

    extractTextFromNode(aiwContentDiv);  // Start extraction from the main div

    return textValues.join('\n');  // Join the list with newline and return
}


/**
 * Compiles a chat API request and sends it to the server.
 */
function sendMessage() {
    var chatInput = document.getElementById('chatInput');
    var messageContent = chatInput.value.trim();

    if (!messageContent) {
        alert('Please type a message before sending.');
        return;
    }

    chatInput.value = ''; // Clear the input box

    appendChatMessage({
        role: 'USER',
        content: messageContent
    });

    chatMessageContainer.scrollTop = chatMessageContainer.scrollHeight;

    var endpoint = '/api/v1/chat/';
    if (currentConversationId) {
        endpoint += currentConversationId;
    }

    var messageData = {
        help_context_id: help_context_id,
        page_content: loadPageContent(),
        content: messageContent
    };

    console.log(messageData);

    fetch(endpoint, {
        method: 'POST',
        body: JSON.stringify(messageData),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            currentConversationId = data.conversation_id || currentConversationId;
            renderChatMessages(data.messages);
            chatInput.value = ''; // Clear the input box
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Sorry, something went wrong.');
        });
}

/**
 * Toolbox function to start a new chat conversation
 * or continue a previous one.
 */
function chat() {
    // If there's no current conversation, send a starting message
    if (!currentConversationId) {
        let data = {
            help_context_id: help_context_id,
            page_content: loadPageContent()
        };

        fetch('/api/v1/chat/new', {
            method: 'POST',
            body: JSON.stringify(data), // Convert the data object to a JSON string
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json()) // Convert the response to a JavaScript object
            .then(data => {
                currentConversationId = data.id;
                renderChatMessages(data.messages);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Sorry, something went wrong starting the chat.');
            });
    }

    openChatInterface();
}


/**
 * Toolbox function to send instructions to the AI assistant
 */
function send_instructions(system_message_title) {
  // If there's no current conversation, send a starting message
  let data = {
      help_context_id: help_context_id,
      page_content: loadPageContent(),
      system_message_title: system_message_title
  };

  renderChatMessages([{
    role: 'SYSTEM',
    content: "Working on it, please wait. This may take a while..."
  }]);

  fetch('/api/v1/chat/instructions', {
      method: 'POST',
      body: JSON.stringify(data), // Convert the data object to a JSON string
      headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
      }
  })
      .then(response => response.json()) // Convert the response to a JavaScript object
      .then(data => {
          console.log(data);
          currentConversationId = data.id;
          renderChatMessages(data.messages);
      })
      .catch(error => {
          console.error('Error:', error);
          alert('Sorry, something went wrong starting the chat.');
      });

  openChatInterface();
}

/**
 * Toolbox function to start a help chat conversation
 */
function help_chat() {
    // This can be updated similarly when you implement the chat feature
    alert('Help chat');
}


// EVENT LISTENERS

// Floating Action Button + Context Menu event listener
document.getElementById('aiToolboxButton').addEventListener('click', toggleContextMenu);

// chatInterface button event listener
document.getElementById('sendButton').addEventListener('click', sendMessage);

// chatInput event listener to send message on Enter key
document.getElementById('chatInput').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // Prevent the default behavior (newline in textarea, form submission, etc.)
        sendMessage();  // Call the function to send the message
    }
});
