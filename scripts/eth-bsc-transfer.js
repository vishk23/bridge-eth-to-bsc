const BridgeEth = artifacts.require('./BridgeEth.sol');

const privKey = '0x467199271803e5e07f824067e95e35498d629370583d2b8dce8a43aabf8a3899';

module.exports = async done => {
  nonce = 2; //Need to increment this for each new transfer
  const accounts = await web3.eth.getAccounts();
  const bridgeEth = await BridgeEth.deployed();
  const amount = 42;
  const message = web3.utils.soliditySha3(
    {t: 'address', v: accounts[0]},
    {t: 'address', v: accounts[0]},
    {t: 'uint256', v: amount},
    {t: 'uint256', v: nonce},
  ).toString('hex');
  const { signature } = web3.eth.accounts.sign(
    message, 
    privKey
  ); 
  await bridgeEth.burn(accounts[0], amount, nonce, signature);
  done();
}

