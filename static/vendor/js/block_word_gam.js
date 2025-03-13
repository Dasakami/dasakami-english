const gameCanvas = document.getElementById("gameCanvas");
const ctx = gameCanvas.getContext("2d");

const pieceCanvases = [
  document.getElementById("piece1"),
  document.getElementById("piece2"),
  document.getElementById("piece3")
];

const pieceContexts = pieceCanvases.map((canvas) => canvas.getContext("2d"));

// Set dimensions for piece canvases
pieceCanvases.forEach((canvas) => {
  canvas.width = 100;
  canvas.height = 100;
});

// Gameboard dimensions
const rows = 8;
const cols = 8;
const blockSize = 300 / cols; // Canvas is 300x300

// Set game canvas size
gameCanvas.width = 300;
gameCanvas.height = 300;

const grid = Array.from({ length: rows }, () => Array(cols).fill(0));
const colors = ["#f54242", "#f5d142", "#42f554", "#4287f5", "#a142f5"];

let score = 0;
let highScore = parseInt(localStorage.getItem("highScore")) || 0;
let displayedScore = 0;
let displayedHighScore = highScore;

// Update the high score on the page
document.getElementById("highScore").innerText = highScore;

// Pieces storage
let currentPieces = [];
let draggingPiece = null;
let offsetX = 0;
let offsetY = 0;
let mouseX = 0;
let mouseY = 0;

// Draw Block
function drawBlock(ctx, x, y, color, size) {
  ctx.fillStyle = color;
  ctx.fillRect(x * size, y * size, size, size);
  ctx.strokeStyle = "#000";
  ctx.strokeRect(x * size, y * size, size, size);
}

// Draw Game Grid
function drawGrid() {
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (grid[row][col] !== 0) {
        drawBlock(ctx, col, row, colors[grid[row][col] - 1], blockSize);
      } else {
        ctx.strokeStyle = "#333";
        ctx.strokeRect(col * blockSize, row * blockSize, blockSize, blockSize);
      }
    }
  }
}

// Generate Random Pieces
function generateRandomPiece() {
  const shapes = [
    [[1, 1, 1]], // Horizontal line
    [[1], [1], [1]], // Vertical line
    [
      [1, 1],
      [1, 1]
    ], // Square
    [
      [1, 1, 0],
      [0, 1, 1]
    ], // Z-shape
    [
      [0, 1, 1],
      [1, 1, 0]
    ] // S-shape
  ];

  const shape = shapes[Math.floor(Math.random() * shapes.length)];
  const color = Math.floor(Math.random() * colors.length) + 1;

  return { shape, color };
}

// Draw a piece on a specific canvas
function drawPiece(canvasCtx, piece, size) {
  canvasCtx.clearRect(0, 0, 100, 100);
  piece.shape.forEach((row, rIdx) => {
    row.forEach((cell, cIdx) => {
      if (cell !== 0) {
        drawBlock(canvasCtx, cIdx, rIdx, colors[piece.color - 1], size);
      }
    });
  });
}

// Generate and display three pieces
function generateAndDisplayPieces() {
  currentPieces = [
    generateRandomPiece(),
    generateRandomPiece(),
    generateRandomPiece()
  ];

  currentPieces.forEach((piece, index) => {
    const canvasCtx = pieceContexts[index];
    drawPiece(canvasCtx, piece, 30);
  });
}

// Check if a piece can be placed at a specific position
function canPlacePiece(piece, gridX, gridY) {
  const { shape } = piece;
  for (let r = 0; r < shape.length; r++) {
    for (let c = 0; c < shape[r].length; c++) {
      if (shape[r][c] === 1) {
        const targetX = gridX + c;
        const targetY = gridY + r;
        if (
          targetX < 0 ||
          targetX >= cols ||
          targetY < 0 ||
          targetY >= rows ||
          grid[targetY][targetX] !== 0
        ) {
          return false;
        }
      }
    }
  }
  return true;
}

// Place a piece on the grid
function placePiece(piece, gridX, gridY) {
  const { shape, color } = piece;
  shape.forEach((row, rIdx) => {
    row.forEach((cell, cIdx) => {
      if (cell === 1) {
        const targetX = gridX + cIdx;
        const targetY = gridY + rIdx;
        grid[targetY][targetX] = color;
      }
    });
  });

  checkAndClearLines();
  drawGrid();
}

// Check and clear full rows or columns
function checkAndClearLines() {
  let linesCleared = 0;

  // Check rows
  for (let row = 0; row < rows; row++) {
    if (grid[row].every((cell) => cell !== 0)) {
      grid[row].fill(0);
      linesCleared++;
    }
  }

  // Check columns
  for (let col = 0; col < cols; col++) {
    let fullColumn = true;
    for (let row = 0; row < rows; row++) {
      if (grid[row][col] === 0) {
        fullColumn = false;
        break;
      }
    }

    if (fullColumn) {
      for (let row = 0; row < rows; row++) {
        grid[row][col] = 0;
      }
      linesCleared++;
    }
  }

  // Update score with animation
  const pointsToAdd = linesCleared * 10;
  animateScore(pointsToAdd);
}

// Animate the score increment
function animateScore(pointsToAdd) {
  const targetScore = score + pointsToAdd;

  const interval = setInterval(() => {
    if (displayedScore < targetScore) {
      displayedScore++;
      document.getElementById("score").innerText = displayedScore;
    } else {
      clearInterval(interval);
    }
  }, 50);

  score = targetScore;

  // Animate high score if surpassed
  if (score > highScore) {
    animateHighScore(score);
  }
}

// Animate the high score increment
function animateHighScore(newHighScore) {
  const interval = setInterval(() => {
    if (displayedHighScore < newHighScore) {
      displayedHighScore++;
      document.getElementById("highScore").innerText = displayedHighScore;
    } else {
      clearInterval(interval);
    }
  }, 50);

  highScore = newHighScore;
  localStorage.setItem("highScore", highScore);
}

// Mouse Event Handlers
function handleMouseDown(e, index) {
  if (!currentPieces[index]) return;

  const rect = pieceCanvases[index].getBoundingClientRect();
  offsetX = e.clientX - rect.left;
  offsetY = e.clientY - rect.top;

  draggingPiece = currentPieces[index];
}

function handleMouseMove(e) {
  if (!draggingPiece) return;

  mouseX = e.clientX - gameCanvas.offsetLeft;
  mouseY = e.clientY - gameCanvas.offsetTop;

  ctx.clearRect(0, 0, gameCanvas.width, gameCanvas.height);
  drawGrid();

  // Draw the dragging piece following the mouse
  draggingPiece.shape.forEach((row, rIdx) => {
    row.forEach((cell, cIdx) => {
      if (cell !== 0) {
        const drawX = Math.floor((mouseX - offsetX) / blockSize) + cIdx;
        const drawY = Math.floor((mouseY - offsetY) / blockSize) + rIdx;
        drawBlock(
          ctx,
          drawX,
          drawY,
          colors[draggingPiece.color - 1],
          blockSize
        );
      }
    });
  });
}

function handleMouseUp(e) {
  if (!draggingPiece) return;

  const gridX = Math.floor((mouseX - offsetX) / blockSize);
  const gridY = Math.floor((mouseY - offsetY) / blockSize);

  if (canPlacePiece(draggingPiece, gridX, gridY)) {
    placePiece(draggingPiece, gridX, gridY);

    const pieceIndex = currentPieces.indexOf(draggingPiece);
    pieceContexts[pieceIndex].clearRect(0, 0, 100, 100);
    currentPieces[pieceIndex] = null;

    if (currentPieces.every((p) => p === null)) {
      generateAndDisplayPieces();
    }
  }

  draggingPiece = null;
  ctx.clearRect(0, 0, gameCanvas.width, gameCanvas.height);
  drawGrid();
}

// Add Event Listeners
pieceCanvases.forEach((canvas, index) => {
  canvas.addEventListener("mousedown", (e) => handleMouseDown(e, index));
  document.addEventListener("mousemove", handleMouseMove);
  document.addEventListener("mouseup", handleMouseUp);
});

// Initialize the game
function initGame() {
  grid.forEach((row) => row.fill(0));
  score = 0;
  displayedScore = 0;
  document.getElementById("score").innerText = displayedScore;
  document.getElementById("highScore").innerText = highScore;
  drawGrid();
  generateAndDisplayPieces();
}

initGame();
