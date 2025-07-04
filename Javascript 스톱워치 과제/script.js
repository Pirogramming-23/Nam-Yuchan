let timer;
let allSelected = false; 
let running = false;
let startTime;
let elapsedTime = 0;
let recordCount = 0;
const recordList = document.getElementById('recordList');
const displaySeconds = document.getElementById('seconds');
const displayMilliseconds = document.getElementById('milliseconds');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');
const deleteSelectedBtn = document.getElementById('deleteSelectedBtn');
const selectAllBtn = document.getElementById('selectAllBtn');



function formatTime(ms) {
    let milliseconds = Math.floor((ms % 1000) / 10);
    let seconds = Math.floor((ms / 1000) % 60);

    return {
        seconds: String(seconds).padStart(2, '0'),
        milliseconds: String(milliseconds).padStart(2, '0')
    };
}

function updateDisplay() {
    const time = formatTime(elapsedTime);
    displaySeconds.textContent = time.seconds;
    displayMilliseconds.textContent = time.milliseconds;
}

function startTimer() {
    if (!running) {
        running = true;
        startTime = Date.now() - elapsedTime;
        timer = setInterval(() => {
            elapsedTime = Date.now() - startTime;
            updateDisplay();
        }, 10);
        startBtn.disabled = true;
        pauseBtn.disabled = false;
    }
}

function pauseTimer() {
    if (running) {
        running = false;
        clearInterval(timer);
        startBtn.disabled = false;
        pauseBtn.disabled = true;

        addRecord();
    }
}

function resetTimer() {
    running = false;
    clearInterval(timer);
    elapsedTime = 0;
    updateDisplay();
    startBtn.disabled = false;
    pauseBtn.disabled = true;
}

function addRecord() {
    recordCount++;
    const time = formatTime(elapsedTime);
    const recordText = `${time.seconds}:${time.milliseconds}`;

    const listItem = document.createElement('li');
    listItem.innerHTML = `
        <input type="checkbox" class="record-checkbox">
        <span>${recordText}</span>
    `;
    recordList.prepend(listItem);

    allSelected = false;
    selectAllBtn.classList.remove('checked');
}


function deleteSelectedRecords() {
    const checkboxes = document.querySelectorAll('.record-checkbox:checked');
    if (checkboxes.length === 0) {

        return; 
    }
        checkboxes.forEach(checkbox => {
            checkbox.closest('li').remove();
        });
        reorderRecords();
        allSelected = false;
        selectAllBtn.classList.remove('checked');

}

function toggleSelectAllRecords() {
    allSelected = !allSelected;
    const checkboxes = document.querySelectorAll('.record-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.checked = allSelected;
    });

    if (allSelected) {
        selectAllBtn.classList.add('checked');
    } else {
        selectAllBtn.classList.remove('checked');
    }
}

function reorderRecords() {
    const listItems = recordList.querySelectorAll('li');
    recordCount = 0; 
    for (let i = listItems.length - 1; i >= 0; i--) {
        const item = listItems[i];
        recordCount++;
        const span = item.querySelector('span');
        const originalText = span.textContent;
        const timePart = originalText.substring(originalText.indexOf('.') - 2);
    }
}

startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);
deleteSelectedBtn.addEventListener('click', deleteSelectedRecords);
selectAllBtn.addEventListener('click', toggleSelectAllRecords);

resetTimer();