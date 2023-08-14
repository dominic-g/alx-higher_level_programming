#!/usr/bin/node
//A script that prints a message depending of the number of arguments passed

const totalArguments = process.argv.length - 2;
if (totalArguments === 0) {
  console.log('No argument');
} else if (totalArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
