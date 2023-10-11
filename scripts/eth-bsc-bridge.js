
// DO NOT USE THIS SCRIPT IN PRODUCTION


const Web3 = require('web3');
const BridgeEth = require('../build/contracts/BridgeEth.json');
const BridgeBsc = require('../build/contracts/BridgeBsc.json');

//const web3Eth = new Web3('wss://mainnet.infura.io/ws/v3/e971888c0cc6430ba15fd65c2d60152e');
const web3Eth = new Web3('HTTP://127.0.0.1:7979');
const web3Bsc = new Web3('HTTP://127.0.0.1:6969');
const adminPrivKey = '0x52ff694bda28b2b57026d89600c8675585f13ef79fa3e32694ad55d93ba24f45';
const { address: admin } = web3Bsc.eth.accounts.wallet.add(adminPrivKey);

const bridgeEth = new web3Eth.eth.Contract(
  BridgeEth.abi,
  BridgeEth.networks['1678146187539'].address
);

const bridgeBsc = new web3Bsc.eth.Contract(
  BridgeBsc.abi,
  BridgeBsc.networks['4447'].address
);

bridgeEth.events.Transfer(
  {fromBlock: 0, step: 0}
)
.on('data', async event => {
  const { from, to, amount, date, nonce, signature } = event.returnValues;

  const tx = bridgeBsc.methods.mint(from, to, amount, nonce, signature);
  const [gasPrice, gasCost] = await Promise.all([
    web3Bsc.eth.getGasPrice(),
    tx.estimateGas({from: admin}),
  ]);
  const data = tx.encodeABI();
  const txData = {
    from: admin,
    to: bridgeBsc.options.address,
    data,
    gas: gasCost,
    gasPrice
  };
  const receipt = await web3Bsc.eth.sendTransaction(txData);
  console.log(`Transaction hash: ${receipt.transactionHash}`);
  console.log(`
    Processed transfer:
    - from ${from} 
    - to ${to} 
    - amount ${amount} tokens
    - date ${date}
    - nonce ${nonce}
  `);
});

(async function wait () {
  if (true) setTimeout(wait, 1000000);
})();
