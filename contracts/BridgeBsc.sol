pragma solidity ^0.5.0;

import './BridgeBase.sol';

contract BridgeBsc is BridgeBase {
  constructor(address token) public BridgeBase(token) {}
}
