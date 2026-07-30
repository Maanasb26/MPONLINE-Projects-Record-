const uploadBtn = document.getElementById("upload-btn");
const sendBtn = document.getElementById("send-btn");

const pdfInput = document.getElementById("pdf");
const questionInput = document.getElementById("question");

const uploadStatus = document.getElementById("upload-status");
const chat = document.getElementById("chat");


// =============================
// Utility Functions
// =============================

function scrollToBottom() {
    chat.scrollTop = chat.scrollHeight;
}

function addUserMessage(message) {

    chat.innerHTML += `
    <div class="message user">

        <div class="bubble">
            ${message}
        </div>

        <div class="avatar">
            👤
        </div>

    </div>
    `;

    scrollToBottom();
}

function addBotMessage(message) {

    chat.innerHTML += `
    <div class="message bot">

        <div class="avatar">
            🤖
        </div>

        <div class="bubble">
            ${message}
        </div>

    </div>
    `;

    scrollToBottom();
}

function addTypingIndicator() {

    chat.innerHTML += `
    <div class="message bot" id="typing-message">

        <div class="avatar">
            🤖
        </div>

        <div class="bubble">

            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>

        </div>

    </div>
    `;

    scrollToBottom();
}

function removeTypingIndicator() {

    const typing = document.getElementById("typing-message");

    if (typing) {
        typing.remove();
    }

}


// =============================
// Upload PDF
// =============================

uploadBtn.onclick = async () => {

    const file = pdfInput.files[0];

    if (!file) {

        alert("Please choose a PDF.");

        return;
    }

    uploadBtn.disabled = true;

    uploadStatus.innerHTML =
        "⏳ Uploading and indexing document...";

    const formData = new FormData();

    formData.append("pdf", file);

    try {

        const response = await fetch("/upload", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        uploadStatus.innerHTML = `
        ✅ <strong>${file.name}</strong><br>
        Successfully indexed ${data.chunks} chunks.
        `;

        addBotMessage(
            `Your document <strong>${file.name}</strong> has been uploaded successfully.<br><br>You can now ask questions about it.`
        );

    }

    catch (error) {

        uploadStatus.innerHTML =
            "❌ Upload Failed";

        addBotMessage(
            "Something went wrong while uploading the document."
        );

        console.error(error);

    }

    uploadBtn.disabled = false;

};


// =============================
// Ask Question
// =============================

async function askQuestion() {

    const question = questionInput.value.trim();

    if (question === "") return;

    addUserMessage(question);

    questionInput.value = "";

    sendBtn.disabled = true;

    questionInput.disabled = true;

    addTypingIndicator();

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                question: question

            })

        });

        const data = await response.json();

        removeTypingIndicator();

        addBotMessage(data.answer);

    }

    catch (error) {

        removeTypingIndicator();

        addBotMessage(
            "Sorry, something went wrong while generating the answer."
        );

        console.error(error);

    }

    sendBtn.disabled = false;

    questionInput.disabled = false;

    questionInput.focus();

}


// =============================
// Events
// =============================

sendBtn.addEventListener("click", askQuestion);

questionInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        event.preventDefault();

        askQuestion();

    }

});

