const quizData = [
    {
        question: "What is the supreme law of the land?",
        options: ["The Constitution", "The Bill of Rights", "The Declaration of Independence", "The Federalist Papers"],
        correct: 0
    },
    {
        question: "What do we call the first ten amendments to the Constitution?",
        options: ["The Bill of Rights", "The Articles of Confederation", "The Preamble", "The Amendments"],
        correct: 0
    },
    {
        question: "How many amendments does the Constitution have?",
        options: ["27", "10", "23", "50"],
        correct: 0
    }
];

let currentQuestionIndex = 0;
let correctAnswers = 0;
let incorrectAnswers = 0;
let selectedOptions = [];
let previousSelectedButton = null; // Variable to keep track of the previously selected button

function loadQuestion(index) {
    const questionElement = document.getElementById("question");
    const optionsContainer = document.getElementById("options-container");
    const nextButton = document.getElementById("next-button");
    const highlightButton = document.getElementById("highlight-button");

    questionElement.textContent = quizData[index].question;
    optionsContainer.innerHTML = "";

    quizData[index].options.forEach((option, i) => {
        const button = document.createElement("button");
        button.classList.add("option");
        button.textContent = option;
        button.onclick = () => selectOption(button, i);
        optionsContainer.appendChild(button);
    });

    nextButton.style.display = "none"; // Hide next button initially
    highlightButton.style.display = index === quizData.length - 1 ? "block" : "none"; // Show on last question
}

function selectOption(button, selected) {
    const currentQuestion = quizData[currentQuestionIndex];

    // If there was a previously selected option, restore its color
    if (previousSelectedButton) {
        previousSelectedButton.classList.remove("highlight"); // Remove highlight from previous option
    }

    // Highlight the newly selected option
    button.classList.add("highlight"); // Highlight the new selection
    previousSelectedButton = button; // Update the previous button

    // Store the selected option
    const selectedOption = currentQuestion.options[selected];
    selectedOptions[currentQuestionIndex] = {
        question: currentQuestion.question,
        selectedOption: selectedOption,
        correctOption: currentQuestion.options[currentQuestion.correct]
    };

    // Check if the answer is correct
    if (selected === currentQuestion.correct) {
        correctAnswers++;
    } else {
        incorrectAnswers++;
    }

    // Show the next button only after selection
    const nextButton = document.getElementById("next-button");
    const highlightButton = document.getElementById("highlight-button");

    if (currentQuestionIndex < quizData.length - 1) {
        nextButton.style.display = "block"; // Show next button
    } else {
        showResults();
    }
}

function loadNextQuestion() {
    currentQuestionIndex++;
    loadQuestion(currentQuestionIndex);
}

function highlightKey() {
    alert("Highlight key information about this question and its options for further review.");
}

function showResults() {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = `
        <div class="result-container">
            <h2 class="result-title">Quiz Completed</h2>
            <div class="result-summary">
                <p class="result-text">You answered <strong>${correctAnswers}</strong> questions correctly.</p>
                <p class="result-text">You answered <strong>${incorrectAnswers}</strong> questions incorrectly.</p>
            </div>
            <h3 class="your-results-title">Your Detailed Results:</h3>
            <ul class="results-list">
                ${selectedOptions.map((result, i) => `
                    <li class="result-item">
                        <strong>Question ${i + 1}:</strong> ${result.question}<br>
                        <strong>Your Answer:</strong> <span class="${result.selectedOption === result.correctOption ? 'correct-answer' : 'wrong-answer'}">${result.selectedOption}</span><br>
                        <strong>Correct Answer:</strong> <span class="correct-answer">${result.correctOption}</span>
                    </li>
                `).join('')}
            </ul>
            <div id="party-celebration" class="party-celebration">
                🎉🎉 Congratulations! 🎉🎉<br>
                <p>You answered more than 50% of the questions correctly!</p>
            </div>
        </div>
    `;

    // Trigger party animation if more than one question is answered correctly
    if (correctAnswers > Math.floor(quizData.length / 2)) {
        const partyCelebration = document.getElementById("party-celebration");
        partyCelebration.style.display = "block"; // Show the celebration
        setTimeout(() => {
            partyCelebration.classList.add("animation"); // Start the animation
        }, 100); // Delay to ensure it's visible

        // Hide the celebration after animation
        setTimeout(() => {
            partyCelebration.style.display = "none"; // Hide celebration after a short time
        }, 4000); // Duration for which the celebration is displayed (increased to 4 seconds)
    }
}


window.onload = () => {
    loadQuestion(currentQuestionIndex);
};
