// script.js
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const wordInput = document.getElementById('wordInput');
const scoreDisplay = document.getElementById('score');

canvas.width = 800;
canvas.height = 600;

let score = 0;
const words = [];
const projectiles = [];
const wordList = [
  'cyber', 'den', 'neo', 'code', 'pixel', 'matrix', 'glitch', 'synth', 'byte', 'virus',
  'quantum', 'laser', 'drone', 'robot', 'ai', 'data', 'cloud', 'server', 'worm', 'firewall',
  'encrypt', 'decrypt', 'binary', 'trazim', 'network', 'signal', 'error', 'debug', 'loop', 'syntax'
];
const fallingSpeed = 2;
const projectileSpeed = 5;




class FallingWord {
  constructor(word, x, y) {
    this.word = word;
    this.x = x;
    this.y = y;
  }

  draw() {
    ctx.fillStyle = '#00ffcc';
    ctx.font = '24px Orbitron';
    ctx.fillText(this.word, this.x, this.y);
  }

  update() {
    this.y += fallingSpeed;
  }
}

class Projectile {
  constructor(x, y, target) {
    this.x = x;
    this.y = y;
    this.target = target;
    this.width = 5;
    this.height = 10;
  }

  draw() {
    ctx.fillStyle = '#ff00ff';
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }

  update() {
    // Move projectile toward the target word
    const targetX = this.target.x + ctx.measureText(this.target.word).width / 2;
    const targetY = this.target.y - 12; // Adjust for word height
    const angle = Math.atan2(targetY - this.y, targetX - this.x);
    this.x += Math.cos(angle) * projectileSpeed;
    this.y += Math.sin(angle) * projectileSpeed;
  }
}

class Ship {
  constructor() {
    this.x = canvas.width / 2 - 25;
    this.y = canvas.height - 50;
    this.width = 50;
    this.height = 50;
  }

  draw() {
    ctx.fillStyle = '#00ffcc';
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }

  shoot(target) {
    const projectile = new Projectile(this.x + this.width / 2 - 2.5, this.y, target);
    projectiles.push(projectile);
  }
}

const ship = new Ship();

function spawnWord() {
  const word = wordList[Math.floor(Math.random() * wordList.length)];
  const x = Math.random() * (canvas.width - 100);
  const y = 0;
  words.push(new FallingWord(word, x, y));
}

function drawScore() {
  scoreDisplay.textContent = `Score: ${score}`;
}

function update() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw ship
  ship.draw();

  // Update and draw words
  words.forEach((word, index) => {
    word.update();
    word.draw();

    // Check if word goes off screen
    if (word.y > canvas.height) {
      words.splice(index, 1);
    }
  });

  // Update and draw projectiles
  projectiles.forEach((projectile, pIndex) => {
    projectile.update();
    projectile.draw();

    // Check collision with the target word
    if (
      projectile.x < projectile.target.x + ctx.measureText(projectile.target.word).width &&
      projectile.x + projectile.width > projectile.target.x &&
      projectile.y < projectile.target.y &&
      projectile.y + projectile.height > projectile.target.y - 24
    ) {
      // Collision detected
      words.splice(words.indexOf(projectile.target), 1);
      projectiles.splice(pIndex, 1);
      score++;
    }

    // Remove projectiles that go off screen
    if (projectile.y + projectile.height < 0) {
      projectiles.splice(pIndex, 1);
    }
  });

  drawScore();
  requestAnimationFrame(update);
}

function checkInput(event) {
  if (event.key === 'Enter') {
    const typedWord = wordInput.value.trim().toLowerCase();
    if (typedWord) {
      // Find the matching word
      const targetWord = words.find(word => word.word.toLowerCase() === typedWord);
      if (targetWord) {
        ship.shoot(targetWord); // Shoot a projectile at the target word
      }
      wordInput.value = ''; // Clear the input field
    }
  }
}

wordInput.addEventListener('keydown', checkInput);

setInterval(spawnWord, 1500); // Spawn words faster for more action
update();