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
    let userInput = await getInput("enter task name\n");
    
    // {
    //   userInput = string;
    
    //   console.log("Your task is " + userInput);
    
    //   // close input stream
    //   rl.close();
    // });

}

// 
// runApp();




