async function sendMessage(message) {
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.classList.add("active");

  // Show user's message
  const userDiv = document.createElement("div");
  userDiv.className = "message user-message";
  userDiv.textContent = message;
  chatBox.appendChild(userDiv);

  // Show loading message
  const loadingDiv = document.createElement("div");
  loadingDiv.className = "message bot-message loading";
  loadingDiv.textContent = "Bot is typing...";
  chatBox.appendChild(loadingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    // Send message to FastAPI backend
    const response = await fetch("/get", {
      method: "POST",
      body: new URLSearchParams({ user_message: message }),
    });

    const data = await response.json();

    // Remove loading message
    chatBox.removeChild(loadingDiv);

    // Show bot's reply
    const botDiv = document.createElement("div");
    botDiv.className = "message bot-message";
    botDiv.innerHTML = formatBotReply(data.response);
    chatBox.appendChild(botDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

  } catch (error) {
    console.error("Error sending message:", error);
    chatBox.removeChild(loadingDiv);

    const errorDiv = document.createElement("div");
    errorDiv.className = "message bot-message error";
    errorDiv.textContent = "Sorry, there was an error connecting to the bot.";
    chatBox.appendChild(errorDiv);
  }
}

function formatBotReply(text) {
  const paragraphs = text.split("\n").filter(p => p.trim() !== "");
  return paragraphs.map(p => `<p>${p}</p>`).join("");
}

// Send on button click
document.getElementById("send-btn").addEventListener("click", () => {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();
  sendMessage(message);
  userInput.value = "";
});

// Send on Enter key
document.getElementById("user-input").addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    const message = e.target.value.trim();
    sendMessage(message);
    e.target.value = "";
  }
});

// Send on option button click
document.querySelectorAll(".options button").forEach((button) => {
  button.addEventListener("click", () => {
    const message = button.textContent.trim();
    sendMessage(message);
  });
});
