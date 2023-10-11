pragma solidity ^0.5.0;

import './TokenBase.sol';

contract TokenEth is TokenBase {
  constructor() public TokenBase('ETH Token', 'ETK') {}
}
