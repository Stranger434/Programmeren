products = [
    {
        title: 'eieren',
        weight: 200
    },
    {
        title: 'melk',
        weight: 400
    },
    {
        title: 'kaas',
        weight: 500
    },
]


console.log(products[0].title);

function calcTotal(){
    let lineTotals = document.querySelectorAll('.line_total')
    console.dir(lineTotals)
    let total = 0;
    for (let lineTotal of lineTotals){
        total += Number(lineTotal.textContent|| '0');
    }
    let totalElement = document.getElementById('total')
    totalElement.textContent = total.toString();
}

function calcLineTotal(event){
    let amount = Number(this.value);
    let total = this.palletWeight * amount

    if (amount < 0) {
        this.value = '0';
        amount = 0;
        alert('cannot go below 0')
    }
    if (amount > 10) {
        this.value = '10';
        amount = 10;
        alert('cannot go over 10')
    }

    this.lineTotal.textContent = total;
    calcTotal();
}

// loop door indexen van array products
// python = for index in range(len(products))
for (let index in products){
    var checkerContainer = document.getElementById('checker')
    var palletLine = document.createElement('p');
    // palletLine.textContent = 'pallet'
    checkerContainer.appendChild(palletLine);

    var palletTitle = document.createElement('label');
    palletTitle.textContent = products[index].title;
    palletLine.appendChild(palletTitle)

    var palletInput = document.createElement('input');
    palletInput.id = 'input_0'
    palletInput.type = 'number'
    palletInput.min = '0'
    palletInput.max = '10'
    palletInput.addEventListener('change', calcLineTotal);
    palletLine.appendChild(palletInput);

    var palletWeight = document.createElement('span');
    palletWeight.textContent = products[index].weight + 'kg';
    palletLine.appendChild(palletWeight);

    var lineTotalDisplay = document.createElement('span');
    lineTotalDisplay.textContent = 0;
    lineTotalDisplay.classList.add('line_total');
    palletLine.appendChild(lineTotalDisplay);


    palletInput.lineTotal = lineTotalDisplay;
    palletInput.palletWeight = products[index].weight
    }



