const startButton = document.getElementById("start");
const nameInput = document.getElementById("name-input");
const taskInput = document.getElementById("task-input");

function onload() {
    startButton.onclick = () => {
        console.log("Hello, World!");
        const data = {
            name: nameInput.value,
            studying: taskInput.value,
        };
        fetch("/api/start", {
            method: "POST",
            body: data,
        });

    };
}

onload()
