pragma solidity ^0.5.0;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract TokenBase is ERC20 {
  address public admin;

  constructor(string memory name, string memory symbol) public ERC20() {
    admin = msg.sender;
  }

  function updateAdmin(address newAdmin) external {
    require(msg.sender == admin, 'only admin');
    admin = newAdmin;
  }

  function mint(address to, uint amount) external {
    require(msg.sender == admin, 'only admin');
    _mint(to, amount);
  }

  function burn(address owner, uint amount) external {
    require(msg.sender == admin, 'only admin');
    _burn(owner, amount);
  }
}

