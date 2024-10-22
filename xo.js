const cells = document.querySelectorAll('.cell');
const statusDisplay = document.getElementById('status');
const resetButton = document.getElementById('resetBtn');
const questionDisplay = document.getElementById('question');
const optionsDisplay = document.getElementById('options');

let currentPlayer = 'X';
let gameActive = true;
let gameState = ["", "", "", "", "", "", "", "", ""];
let questions = [
    {
        question: "What is the supreme law of the land?",
        options: ["Constitution", "Bill of Rights", "Common Law", "Statutory Law"],
        answer: "Constitution"
    },
    {
        question: "Which article of the Constitution provides for the establishment of a High Court?",
        options: ["Article 124", "Article 226", "Article 14", "Article 32"],
        answer: "Article 226"
    },
    {
        question: "What is the minimum age to contest for the Lok Sabha?",
        options: ["18 years", "21 years", "25 years", "30 years"],
        answer: "25 years"
    },
    {
        question: "Who is known as the Father of the Constitution of India?",
        options: ["Jawaharlal Nehru", "B.R. Ambedkar", "Gandhi", "Sardar Patel"],
        answer: "B.R. Ambedkar"
    }
];
let currentQuestionIndex = 0;

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

// Function to disable the game board
const disableGame = () => {
    cells.forEach(cell => cell.removeEventListener('click', handleCellClick));
};

// Function to enable the game board
const enableGame = () => {
    cells.forEach(cell => cell.addEventListener('click', handleCellClick));
};

// Function to display the current question and options
const displayQuestion = () => {
    const currentQuestion = questions[currentQuestionIndex];
    questionDisplay.textContent = currentQuestion.question;
    optionsDisplay.innerHTML = '';

    currentQuestion.options.forEach(option => {
        const button = document.createElement('button');
        button.textContent = option;
        button.onclick = () => checkAnswer(option);
        optionsDisplay.appendChild(button);
    });
};

// Check the answer and update the game state
const checkAnswer = (selectedOption) => {
    const correctAnswer = questions[currentQuestionIndex].answer;

    if (selectedOption === correctAnswer) {
        statusDisplay.textContent = `Correct! Player ${currentPlayer}, you can now take your turn.`;
        enableGame(); // Enable the game for the player to make their move
    } else {
        statusDisplay.textContent = `Incorrect! Player ${currentPlayer} loses their turn.`;
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X'; // Switch player
        statusDisplay.textContent = `Player ${currentPlayer}'s Turn`;
        currentQuestionIndex = (currentQuestionIndex + 1) % questions.length; // Next question
        displayQuestion();
    }
};

// Handle cell click events
const handleCellClick = (event) => {
    const clickedCell = event.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));

    if (gameState[clickedCellIndex] !== "" || !gameActive) {
        return;
    }

    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.textContent = currentPlayer;
    handleResultValidation();
};

// Validate game result
const handleResultValidation = () => {
    let roundWon = false;

    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        if (gameState[a] === "" || gameState[b] === "" || gameState[c] === "") {
            continue;
        }
        if (gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            roundWon = true;
            break;
        }
    }

    if (roundWon) {
        statusDisplay.textContent = `Player ${currentPlayer} has won!`;
        gameActive = false;
        return;
    }

    if (!gameState.includes("")) {
        statusDisplay.textContent = 'Game ended in a draw!';
        gameActive = false;
        return;
    }

    // Switch player and display the next question
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    statusDisplay.textContent = `Player ${currentPlayer}'s Turn`;
    currentQuestionIndex = (currentQuestionIndex + 1) % questions.length; // Next question
    disableGame(); // Disable the game board for the next player
    displayQuestion(); // Show the question for the next player
};

// Reset the game
const resetGame = () => {
    gameActive = true;
    currentPlayer = "X";
    gameState = ["", "", "", "", "", "", "", "", ""];
    statusDisplay.textContent = `Player ${currentPlayer}'s Turn`;
    cells.forEach(cell => cell.textContent = "");
    currentQuestionIndex = 0; // Reset question index
    disableGame(); // Initially disable the game board
    displayQuestion(); // Display the first question
};

// Initialize the game
disableGame(); // Disable the game board at the start
displayQuestion();
resetButton.addEventListener('click', resetGame);



