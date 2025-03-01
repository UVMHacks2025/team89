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

function showMainScreen() {
    startScreen.hidden = true;
    const leaderboard = document.getElementById("leaderboard");
    let table = `
    <table>
        <thead>
            <tr>
                <th>User</th>
                <th>Points</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    `;
    
    table += `
        </tbody>
    </table>
    `;
    leaderboard.innerHTML = table;
}

onload()
