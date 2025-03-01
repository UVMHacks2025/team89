const startScreen = document.getElementById("start-screen");
const mainScreen = document.getElementById("main-screen");
const startButton = document.getElementById("start");
const nameInput = document.getElementById("name-input");
const taskInput = document.getElementById("task-input");

// How long timer is in seconds
let timerLength = 1 * 60 - 55;
let timerTask;

function onload() {
}

startButton.onclick = async () => {
    console.log("Hello, World!");
    const data = {
        name: nameInput.value,
        studying: taskInput.value,
    };
    const response = await fetch("/api/start", {
        method: "POST",
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    });
    const result = await response.json();
    console.log(result);
    showMainScreen(result);
};

function showMainScreen(data) {
    startScreen.hidden = true;
    mainScreen.hidden = false;
    updateLeaderboard(data.leaderboard);

    updateTimer(timerLength);
    timerStart.onclick = () => {
        let start_time = Date.now();

        if (timerTask) {
            clearInterval(timerTask);
            timerTask = null;
        }
        timerTask = setInterval(() => {
            const elapsed = (Date.now() - start_time) / 1000.0;
            let currentSeconds = Math.floor(timerLength - elapsed);
            if (currentSeconds <= 0) {
                currentSeconds = 0;
                timerDone();
            }
            updateTimer(currentSeconds);
        }, 100);
    };
}

const timerStart = document.getElementById("timer-start-button");
const timerContent = document.getElementById("timer-value");
function updateTimer(seconds) {
    console.log(seconds);
    let m = String(Math.floor(seconds / 60)).padStart(2, "0");
    let s = String(seconds % 60).padStart(2, "0");
    timerContent.innerText = `${m}:${s}`;
}

const cat1 = document.getElementById("cat1");
const cat2 = document.getElementById("cat2");
const cat3 = document.getElementById("cat3");
const cats = [ cat1, cat2, cat3 ];

function timerDone() {
    clearInterval(timerTask);
    timerTask = null;
    console.log("Timer done!!!")
    for (const cat of cats) {
        cat.hidden = false;
        cat.classList.add("move-across");
        setTimeout(() => {
            cat.classList.remove("move-across");
            cat.hidden = true;
        }, 2000);
    }
}

function updateLeaderboard(data) {
    const leaderboard = document.getElementById("leaderboard");
    let table = `<table>
        <thead>
            <tr>
                <th>User</th>
                <th>Points</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    `;
    for (const item of data) {
        table += `
        <tr>
            <td>${item.username}</td>
            <td>${item.points}</td>
        </tr>
        `
    }
    
    table += `
        </tbody>
    </table>
    `;
    leaderboard.innerHTML = table;
}

onload()
