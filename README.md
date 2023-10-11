# Smart Contract Bridge Example
This repository showcases a research project focused on smart contract interoperability between Ethereum and Binance Smart Chain (BSC). 
## Technologies Used
- **Truffle**: A development environment, testing framework, and asset pipeline for Ethereum.
- **Ganache**: Part of the Truffle suite, it's a personal blockchain for rapid Ethereum and Corda distributed application development. Used here for Ethereum and BSC simulations.
- **JavaScript (JS)**: The primary scripting language for deployment and testing scripts.
## Setup and Deployment
1. **Install Prerequisites**:
- [Truffle](https://www.trufflesuite.com/truffle)
- [Ganache CLI](https://www.npmjs.com/package/ganache-cli) (Note: The GUI version isn't used in this project.)
2. **Initialize Ganache**: Set up both Ethereum and BSC local chains using Ganache.
3. **Node Version**: Ensure compatibility by using Node version less than v19: `nvm use 18.12.0`.
4.  **Configuration**: Update `truffle-config.js` for correct network setups and set private keys in the respective scripts.
5.  **Migration**: Deploy contracts to both Ethereum and BSC simulated networks.
6.   **Start the Bridge**: Use the provided Python script (`BRIDGE.py`). Ensure correct paths to the contract JSON files.
7.    **Test Transfer**: Use the `eth-bsc-transfer.js` script for testing the bridge functionality.