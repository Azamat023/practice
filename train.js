/* B-TASK (NodeJS)

Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi. */


// ⭐️ Masalaning yechimi


function countNums(str) {
  return str.split("").map(Number).filter(Boolean).length;
}



console.log(countNums("gwefkwgiefgwkb886kdhjk"));









/* A- Task (NodeJS)

Savol: Shunday 2 parametrli functionlarni tuzing,
hamda birinchi parameterdagi so'zdan qatnashfan sonini return qilishi kerak buladi.
Masalan countLetter("e", "engineer") 3ni return qiladi. */

//parameter letter words

//function countLetters (letter, word) {
  //  const splittedWord = word.split("")
    //const filteredWord = splittedWord.filter((ele) => {return ele === letter})
   // return filteredWord.length

//}

//console.log(countLetters("letter", "word"))
