# RTK Token

Users would need to install hardhat and openzepplin to enable them to deploy the RTK Token

The deployed contract is as follows:
[Etherscan Link](https://goerli.etherscan.io/address/0xFc81527762b47819ebD33A89bA31635058E61Ff9)

Additionally, we also worked with DApps such as Pancakeswap to build out a place where users can trade their ethereum or USDC to RTK or the other way around. 

In this case, we used Goerli to imitate Ethereum on the Goerli Testnetwork.
![PancakeSwapImage](https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/PancakeswapTransfer.PNG)

Here is the liquidity of Goerli and RTK that shows the price of RTK for each Goerli coin
![GoerliLiquidity](https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/LiquidityPanacakeSwap.PNG)

Once the token is deployed, users can earn Goerli from a faucet and convert that to RTK. Here is what an RTK token looks like on MetaMask.
![RTKtoken](https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/RTKtoken.PNG)

We used Solidity, openzepplin, and hardhat to deploy the contract with information as follows:
![RTKDeployment]((https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/RTKDeployment.PNG)

Here is the deployment script for the RTK Token:
![DeploymentScript](https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/DeploymentScript.PNG)

And here is the edited hardhat config code using goerli:
![Config](https://github.com/mr-alex-leonov/Recycle-to-Earn/blob/Ritvik/ConfigFile.PNG)
