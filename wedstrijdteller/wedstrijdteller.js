var inputTeams = document.getElementById('input-teams');
var lastScoringTeam = { team1: 0, team2: 0 };
var lastServingTeamNow = null;
var lastServingTeamPrevious = null;

inputTeam1.value = ''; // testdata
inputTeam2.value = ''; // testdata

function start(event) {
    if ((inputTeam1.value.trim() == '') || (inputTeam2.value.trim() == '')) return
    inputTeams.style.display = 'none';
    counterTeam1.counter = 0;
    counterTeam2.counter = 0;
    displayNames();
    displayCounters();
    startServing();
    counterTeam1.addEventListener('click', count);
    counterTeam2.addEventListener('click', count);
    undoButton.addEventListener('click', undo);
}

function displayCounters() {
    counterTeam1.textContent = counterTeam1.counter;
    counterTeam2.textContent = counterTeam2.counter;
}

function startServing() {
    if (!servingTeam2.checked) {
        displayServing(counterTeam1);
        lastServingTeamNow = counterTeam1
    } else if (servingTeam2.checked) {
        displayServing(counterTeam2);  
        lastServingTeamNow = counterTeam2
}}

function displayServing(teamCounter) {
    counterTeam1.classList.remove('serving'); 
    counterTeam2.classList.remove('serving');
    teamCounter.classList.add('serving');
}

startButton.addEventListener('click', start);

function count(event) {
    // Store previous counter values before updating
    this.counter++;
    displayCounters();
    displayServing(this);
    lastScoringTeam = this;

    lastServingTeamPrevious = lastServingTeamNow
    lastServingTeamNow = this;
}

function undo() {
    if (lastScoringTeam === null) return;
    lastScoringTeam.counter--;
    displayCounters();
    lastScoringTeam = null;
    lastServingTeamNow = lastServingTeamPrevious;
    lastServingTeamPrevious = null;
    displayServing(lastServingTeamNow);
}


function displayNames(event) {
    nameTeam1.textContent = inputTeam1.value.trim() || '...';
    nameTeam2.textContent = inputTeam2.value.trim() || '...';
}
inputTeam1.addEventListener('change', displayNames);
inputTeam2.addEventListener('change', displayNames);

function refreshPage() {
    location.reload();
    servingTeam1.checked = false;
    servingTeam2.checked = false;
}

quit.addEventListener('click', refreshPage);
