const operations = {
    '$': (a, b) => a / b,
    '*': (a, b) => a * b,
    '-': (a, b) => a - b,
    '+': (a, b) => a + b,
};
function operate(parts, operator, fn) {
    for (let i = 0; i < parts.length; i++) {
        const token = parts[i];
        if (token === operator) {
            const result = fn(parts[i - 1], parts[i + 1]);
            parts.splice(i - 1, 3, result);
            i = i - 1;
        }
    }
}
function calculate(route) {
    const parts = route
        .split('')
        .reduce(({ parts, currentNumber }, token, i, tokens) => {
            if (operations[token]) {
                parts = [...parts, +currentNumber, token];
                currentNumber = '';
            } else {
                currentNumber += token;
            }
            if (i === tokens.length - 1) {
                return [...parts, +currentNumber];
            }
            return { parts, currentNumber };
        }, {
            parts: [],
            currentNumber: ''
        });
    Object
        .keys(operations)
        .forEach(operation => {
            operate(parts, operation, operations[operation]);
        });
    return isNaN(parts[0]) ? '400: Bad request' : parts[0];
}