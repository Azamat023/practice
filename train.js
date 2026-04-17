/* A- Task (NodeJS)

Savol: Shunday 2 parametrli functionlarni tuzing,
hamda birinchi parameterdagi so'zdan qatnashfan sonini return qilishi kerak buladi.
Masalan countLetter("e", "engineer") 3ni return qiladi. */

//parameter letter words

function countLetters (letter, word) {
    const splittedWord = word.split(" ")
    const filteredWord = splittedWord = splittedWord.filter((ele) => {return ele === letter})
    return filteredWord.length

}

console.log(countLetters("letter", "word"))
