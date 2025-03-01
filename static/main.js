const startScreen = document.getElementById("start-screen");
const mainScreen = document.getElementById("main-screen");
const startButton = document.getElementById("start");
const nameInput = document.getElementById("name-input");
const taskInput = document.getElementById("task-input");

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

    const timerStart = document.getElementById("timer-start-button");
    const timerContent = document.getElementById("timer-value");
    timerStart.onclick = () => {
        let start_time = Date.now();
        let time_length = 1 * 60;

        setInterval(() => {
            const ellapsed = (Date.now() - start_time) / 1000.0;
            let current_seconds = Math.ceil(time_length - ellapsed);
            let m = String(Math.floor(current_seconds / 60)).padStart(2, "0");
            let s = String(current_seconds % 60).padStart(2, "0");
            timerContent.innerText = `${m}:${s}`;
        }, 100);
    };
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
    for (const [name, points] of Object.entries(data)) {
        table += `
        <tr>
            <td>${name}</td>
            <td>${points}</td>
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
