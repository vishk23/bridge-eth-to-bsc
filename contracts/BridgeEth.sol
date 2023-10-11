pragma solidity ^0.5.0;

import './BridgeBase.sol';

contract BridgeEth is BridgeBase {
 constructor(address token) public BridgeBase(token) {}
}
