const words = document.querySelector('[data-words]');
const sentence = document.querySelector('[data-sentence]');
const placeholder = document.querySelector('[data-placeholder]');
const btn = document.querySelector('[data-btn]');
const leaderboard = document.querySelector('[data-leaderboard]');

var entries = [];



function submit() {
	let sen = '',
		wrds = sentence.querySelectorAll('.word'),
		uid = new Date().getTime(),
		entryObj = {};

	[].forEach.call(wrds, (wrd) => {
		sen += `${wrd.innerHTML} `;
	});
	
	entryObj = {
		'uid': uid,
		'sentence': sen,
		'loves': 0
	};
	
	entries.push(entryObj);
	
	updateLeaderboard();
	
	clearBuilder();
}

function updateLeaderboard() {
	let markup = '';
	
	entries = _.sortBy(entries, 'loves').reverse();
		
	leaderboard.innerHTML = '';
		
	entries.forEach((entry, i) => {
		leaderboard.appendChild(buildEntry(entry, i + 1));
	});
}
	
function buildEntry(entry, index) {
	let entryContainer = document.createElement('article');
	
	entryContainer.classList.add('leaderboard__entry');
	entryContainer.innerHTML = `
		<div class="leaderboard__num">
			${index}
		</div>
		<p class="leaderboard__sentence">${entry.sentence}</p>
		<a href="#" class="leaderboard__love fa fa-heart" data-love="${entry.uid}"></a>
		<span class="leaderboard__loves">${entry.loves}</span>
	`;
			
	entryContainer.querySelector('[data-love]').addEventListener('click', (e) => {
		e.preventDefault();
		love(e.currentTarget.getAttribute('data-love'));
	});
	
	return entryContainer;
}

function love(uid) {
	let entry = _.find(entries, {uid: Number(uid)});
	entry.loves++;
	updateLeaderboard();
}

function clearBuilder() {
	let wrds = sentence.querySelectorAll('.word');
	
	[].forEach.call(wrds, (wrd) => {
		words.appendChild(wrd);
	});
	
	resetPlaceholder();
}

function resetPlaceholder() {
	let s = sentence.querySelectorAll('.word');

	if (!s.length) {
		placeholder.style.display = 'block';
	} else {
		placeholder.style.display = 'none';
	}
}

document.addEventListener('DOMContentLoaded', () => {

	var drag = dragula([
		words,
		sentence
	]);

	btn.addEventListener('click', submit);

	drag.on('drop', resetPlaceholder);
	drag.on('cancel', resetPlaceholder);

});