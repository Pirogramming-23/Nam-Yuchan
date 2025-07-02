const number1 = document.getElementById('number1');
const number2 = document.getElementById('number2');
const number3 = document.getElementById('number3');
const attemptsSpan = document.getElementById('attempts');
const resultsDiv = document.getElementById('results');
const submitbtn = document.querySelector('.submit-button');
const gameResultImg = document.getElementById('game-result-img');
let answer = [];
let attempts = 9;
function RandomNumbers() {
    answer = [];
    while (answer.length < 3) {
        const randomnum = Math.floor(Math.random() * 10);
        if (!answer.includes(randomnum)) {
            answer.push(randomnum);
        }
    }
}


function check_numbers() {
    const num1 = number1.value;
    const num2 = number2.value;
    const num3 = number3.value;

    //input이 비어있거나 빈칸 입력하면 input만 초기화
    if (num1 === '' || num2 === '' || num3 === '' || num1 === ' ' || num2 === ' ' || num3 === ' ') {
        number1.value = '';
        number2.value = '';
        number3.value = '';
        number1.focus();
        return;
    }

    const input = [parseInt(num1), parseInt(num2), parseInt(num3)];
    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (input[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(input[i])) {
            balls++;
        }
    }

    attempts--;
    attemptsSpan.textContent = attempts;

    let result = '';
    if (strikes === 3) { //3스트라이크하면 승리
        result = '승리!';
        gameResultImg.src = 'success.png';
        submitbtn.disabled = true; //확인하기 버튼 비활성화
    } else if (strikes === 0 && balls === 0) {
        result = 'O'; //하나도 안겹치면 O로 출력
    } else {
        result = `${strikes}S ${balls}B`; //자리까지 맞으면 s 자리는 안맞지만 정답이 포함되면 b
    }

    const p = document.createElement('p');
    p.textContent = `${input.join('')} - ${result}`;
    resultsDiv.prepend(p);

    if (attempts === 0 && strikes !== 3) {// 실패하면 실패이미지 출력
        gameResultImg.src = 'fail.png';
        submitbtn.disabled = true; //확인하기 버튼 비활성화
        const p = document.createElement('p');
        p = `정답은 ${answer.join('')} 였습니다`;
        resultsDiv.prepend(p);
    }

    number1.value = '';
    number2.value = '';
    number3.value = '';
    number1.focus();
}

number1.addEventListener('input', () => {
    if (number1.value.length === 1) { //첫번째 자리수에 숫자입력하면
        number2.focus();//두번째자리로 이동
    }
});
number2.addEventListener('input', () => {
    if (number2.value.length === 1) {
        number3.focus();
    }
});
number3.addEventListener('input', () => {
    if (number3.value.length === 1) {
        submitbtn.focus();
    }
});

// 엔터 키로 확인 버튼 클릭
document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !submitbtn.disabled) {
        check_numbers();
    }
});
//백스페이스 키로 지움
number2.addEventListener('keydown', (event) => {
    if (event.key === 'Backspace' && number2.value.length === 0) {
        number1.focus(); // number2가 비어있고 백스페이스 누르면 number1로 이동
    }
});

number3.addEventListener('keydown', (event) => {
    if (event.key === 'Backspace' && number3.value.length === 0) {
        number2.focus(); // number3이 비어있고 백스페이스 누르면 number2로 이동
    }
});

function Initialize() { //초기화
    attempts = 9;
    attemptsSpan.textContent = attempts;
    resultsDiv.innerHTML = '';
    number1.value = '';
    number2.value = '';
    number3.value = '';
    gameResultImg.src = '';
    submitbtn.disabled = false;
    number1.focus();
    RandomNumbers();
}
Initialize();