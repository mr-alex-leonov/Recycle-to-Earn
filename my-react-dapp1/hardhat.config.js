require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  path: {
    artifacts: "../src/artifacts",
  },
  networks: {
   hardhat: {
    chainId: 1337
    }
  },
  solidity: "0.8.18",
};
