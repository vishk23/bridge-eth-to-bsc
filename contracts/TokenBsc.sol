pragma solidity ^0.5.0;

import './TokenBase.sol';

contract TokenBsc is TokenBase {
  constructor() public TokenBase('BSC Token', 'BTK') {}
}
