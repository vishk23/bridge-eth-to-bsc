const Web3EthAccounts = require('web3-eth-accounts');

const account = new Web3EthAccounts('ws://localhost:8546');
account.create();
console.log();