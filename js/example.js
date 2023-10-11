const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getInput(promptText) {
    return new Promise((resolve) => {
        rl.question(promptText, resolve);
    });
}

async function runApp() {
    // The prompt() method displays a dialog box that prompts the user for input.
    prompt("chooose your option\n
        1. display TODos\n 2. add new ToDo")
    let userInput = await getInput("enter task name\n");
    switch(userInput){
        case 1: console.log('\nToDos\n')
         console.log(todos)
         case 2: console.log()

    }
    
    // return userInput
    
    // {
    //   userInput = string;
    
    //   console.log("Your task is " + userInput);
    
    //   // close input stream
    //   rl.close();
    // });

}

// 
// runApp();




