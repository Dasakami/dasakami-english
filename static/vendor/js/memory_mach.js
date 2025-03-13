const gameState = {
  selectedCards: [],
  allCards: [],
  cardIcons: ['fa-bolt', 'fa-music', 'fa-graduation-cap', 'fa-gamepad', 'fa-flask', 'fa-cloud', 'fa-rocket', 'fa-pencil'],
  moveCount: 0,
};

//------------------Functions for randomizing array--------------------//
function getRandomInt (max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function randomizeCards (arr) {
  const randomized = [],
        iterations = arr.length;
  for (let i = 0; i < iterations; i++) {
    randomized.push(arr.splice(getRandomInt(arr.length), 1)[0]);
  }
  return randomized;
}
//---------------End of functions for randomizing array------------------//

//**setupDeck for inital population of deck and creating object within gameState object**//
function setupDeck () {
  const cardsRand = randomizeCards(gameState.cardIcons.concat(gameState.cardIcons));
  gameState.moveCount = 0;//set movecount to zero
  document.getElementsByClassName('moves')[0].textContent = 0;//set text content back to zero
  gameState.allCards.length = 0;
  gameState.selectedCards.length = 0;
  addStars();
  document.getElementById('timeCurrent').innerHTML = `Time: 0:00`; //***zero out timer
  let cardClasses = '';
  for (let i = 0; i < cardsRand.length; i++) {
    cardClasses += `<div id="${i}" class="card"><i class="fa ${cardsRand[i]}"></i></div>`;
    gameState.allCards.push (
    {
        'style': cardsRand[i],
        'visible': false//made true in cardSelect()
      }
    );
  }
  document.getElementsByClassName('deck')[0].innerHTML = cardClasses;
}
//*******************End of setupDeck function**************************//

function cardSelect (e) {
  if (e.target.matches('.card')) {
    // document.getElementsByClassName('deck')[0].removeEventListener('click', clickStart);
    const card = e.target;
    if (!gameState.allCards[card.id].visible && gameState.selectedCards.length < 2) {
      flip(card);
      if (gameState.selectedCards.length === 2) {
        removeStars();///***FIX this function!!!
        movesCount();
        moveNumber();
        checkCardMatch(card);
        reset();
      }
    }
  }
}

//****Functions for timer ******//

function timerStart () {
  let timeCurrent = document.getElementById('timeCurrent');
  let timer = document.getElementById('timer');
  let counter = 0;
  
  function startTime () {
    counter++;
    timer.innerHTML = `Time: ${convertSeconds(counter)}`;
    timerStop();
  }
  
  let set = setInterval(startTime, 1000);
  
  function clear () { //used for reset button, called on line 87
    clearInterval(set);
    timer.innerHTML = 'Time: 0:00';
    document.getElementsByClassName('deck')[0].addEventListener('click', clickStart);
  }
  
  function timerStop () { // once the timerStart function is called, how does it stop???
    document.getElementById('reset').addEventListener('click', clear);
    document.getElementById('button').addEventListener('click', clear);
    const cardQty = gameState.allCards.length;
    let visible = 0;
    for (let i = 0; i < cardQty; i++) {
      if (gameState.allCards[i].visible)
        visible++;
    }
    if (visible === cardQty) {
      timeCurrent.innerHTML = `Time: ${convertSeconds(counter)}`;
      clearInterval(set);
      }
  }
}

function clickStart (e) {
  if (e.target.matches('.card')) {
    timerStart();
    document.getElementsByClassName('deck')[0].removeEventListener('click', clickStart);
  }
}

function convertSeconds (s) {
   let minute = Math.floor(s / 60);
   let sec = s % 60;
    sec = sec.toString().padStart(2, '0');
    
    return minute + ':' + sec;
  }
//End of functions for timer//

//***Function to display number of moves***///
function moveNumber () {
  document.getElementsByClassName('moves')[0].textContent = gameState.moveCount;
}
// /////*****Function to count number of moves****//
function movesCount () {
  gameState.moveCount += 1;
}
//*************************End movecount function******************////

//Turnover card when clicked
function flip (card) {
  card.classList.add('open', 'show');
  gameState.allCards[card.id].visible = true;
  gameState.selectedCards.push(card.id);
}

//Checking if two cards match
function checkCardMatch (card) {

  if (gameState.allCards[gameState.selectedCards[0]].style === gameState.allCards[gameState.selectedCards[1]].style) {
    console.log('match');
    for (let i = 0; i < gameState.selectedCards.length; i++) {
      document.getElementsByClassName('card')[`${gameState.selectedCards[i]}`].classList.add('match');
    }
    gameState.selectedCards.length = 0;
  } else {
    console.log('no match');

    for (let i = 0; i < gameState.selectedCards.length; i++) {
      document.getElementsByClassName('card')[`${gameState.selectedCards[i]}`].classList.add('nomatch');
    }
    //need hide function after this executes in a settimout
    setTimeout(
      () => {
        hide();
        gameState.selectedCards.length = 0;
      },
      800
    );
  }
}

//If two cards do not match
function hide () {
  for (let i = 0; i < gameState.selectedCards.length; i++) {
      document.getElementById(gameState.selectedCards[i]).classList.remove('nomatch', 'open', 'show');
      gameState.allCards[gameState.selectedCards[i]].visible = false;
  }
}

//Occurs when game is over
function reset () {
  //if all visible = true, reset code
  const cssTransitionTime = 200;
  const cardQty = gameState.allCards.length;
  let visible = 0;
  for (let i = 0; i < cardQty; i++) {
    if (gameState.allCards[i].visible)
      visible++;
  }
  if (visible === cardQty) { //*****place in other function???
    toggleModal();//***add modal
  }
}

//**Remove and add stars*****//
function removeStars () {
  let star3 = document.getElementsByClassName('stars')[0].getElementsByClassName('fa')[2];
  let star2 = document.getElementsByClassName('stars')[0].getElementsByClassName('fa')[1];
  let star31 = document.getElementsByClassName('stars')[1].getElementsByClassName('fa')[2];
  let star21 = document.getElementsByClassName('stars')[1].getElementsByClassName('fa')[1];
    if (gameState.moveCount === 14) {
      star3.classList.remove('fa-star');
      star31.classList.remove('fa-star');
    } 
  
    if (gameState.moveCount >= 14) {
      star3.classList.add('fa-star-o');
      star31.classList.add('fa-star-o');
    }
    
    if (gameState.moveCount === 23) {
      star2.classList.remove('fa-star');
      star21.classList.remove('fa-star');
    }
    if (gameState.moveCount >= 23) {
      star2.classList.add('fa-star-o');
      star21.classList.add('fa-star-o');
    }
  
}

function addStars () {
  let star3 = document.getElementsByClassName('stars')[0].getElementsByClassName('fa')[2];
  let star2 = document.getElementsByClassName('stars')[0].getElementsByClassName('fa')[1];
  let star31 = document.getElementsByClassName('stars')[1].getElementsByClassName('fa')[2];
  let star21 = document.getElementsByClassName('stars')[1].getElementsByClassName('fa')[1];
      star3.classList.remove('fa-star-o');
      star3.classList.add('fa-star');
      star2.classList.remove('fa-star-o');
      star2.classList.add('fa-star');
      star31.classList.remove('fa-star-o');
      star31.classList.add('fa-star');
      star21.classList.remove('fa-star-o');
      star21.classList.add('fa-star');
      
    }

//********Toggle Modal********///

function toggleModal() {
        removeStars ()
        let score = document.getElementById('score');
        let thinking = document.getElementById('thinking');
        let verdict = document.getElementById('verdict');
        score.textContent = "Your score in moves: " + gameState.moveCount;
        if (gameState.moveCount <= 14) {
          thinking.textContent = "Whoa! You're memory is impeccable!";
        }
        if (gameState.moveCount >= 15 && gameState.moveCount <=23) {
          thinking.textContent = "Your memory is okay!";
        } 
        if (gameState.moveCount > 23) {
          thinking.textContent = "Your memory sucks! See a doctor immediately!";
        }
        
      
        let modal = document.querySelector(".modal");
        modal.classList.toggle("show-modal");
    }

function windowOnClick(event) {
        let modal = document.querySelector(".modal");
          if (event.target === modal) {
            toggleModal();
        }
    }

//Cheat function
function cheat () {
  const styles = [
    'fa-bolt',
    'fa-music',
    'fa-graduation-cap',
    'fa-gamepad',
    'fa-flask',
    'fa-cloud',
    'fa-rocket',
    'fa-pencil'
  ];

  for (let i = 0; i < styles.length; i++) {
    for (let j = 0; j < document.querySelectorAll(`.${styles[i]}`).length; j++) {
      document.querySelectorAll(`.${styles[i]}`)[j].parentNode.click();
    }
  }
}
//end of cheat function

setupDeck();
document.getElementsByClassName('deck')[0].addEventListener('click', cardSelect);
document.getElementById('reset').addEventListener('click', setupDeck);
//**below is for the modal**//
    window.addEventListener("click", windowOnClick);
document.getElementById('button').addEventListener('click', setupDeck);
document.getElementById('button').addEventListener('click', toggleModal);
//***Below is an event listener for the timer
document.getElementsByClassName('deck')[0].addEventListener('click', clickStart);


