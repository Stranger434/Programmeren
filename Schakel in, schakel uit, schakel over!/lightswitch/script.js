var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = 'Switch light On';
document.body.appendChild(btn);
document.body.style.backgroundColor = 'black';

// schijf hier tussen je code

function knop() {
    if (btn.innerHTML == 'Switch light On') {
        document.body.style.backgroundColor = 'yellow';
        console.log('Light is On');
        btn.innerHTML = 'Switch light Off';
    } else {
        btn.innerHTML = 'Switch light On';
        console.log('Light is Off');
        document.body.style.backgroundColor = 'black';
    }
}


btn.addEventListener('click', knop);
// schijf hier tussen je code