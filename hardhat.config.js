
require("@nomicfoundation/hardhat-toolbox");

const privateKey = "011fc640f0d38d8df5cc035324fd550107e920b00ef361c39a1ad8fc22b0132a";

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  defaultNetwork: "goerli",
  networks: {
    hardhat: {},
    goerli: {
      url: "https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
      accounts: [privateKey]
    }
  },
  solidity: {
    compilers: [
      {
        version: "0.8.0",
      },
    ],
  },
};
