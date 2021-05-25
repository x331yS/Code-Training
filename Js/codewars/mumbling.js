function accum(input) {
    return input.split('').reduce((result, currentLetter, index) => {
        const totalCount = index + 1;
        for (let counter = 0; counter < totalCount; counter++) {
            if (counter == 0) {
                result += currentLetter.toUpperCase();
            } else {
                result += currentLetter.toLowerCase();
            }
        }

        if (index != input.length - 1) {
            result += '-';
        }
        return result;
    }, '');
}