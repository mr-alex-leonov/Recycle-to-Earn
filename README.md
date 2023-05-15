# RTK Token

Users would need to install hardhat and openzepplin to enable them to deploy the RTK Token

The deployed contract is as follows:
[Etherscan Link](https://goerli.etherscan.io/address/0xFc81527762b47819ebD33A89bA31635058E61Ff9)

Additionally, we also worked with DApps such as Pancakeswap to build out a place where users can trade their ethereum or USDC to RTK or the other way around. 

In this case, we used Goerli to imitate Ethereum on the Goerli Testnetwork.
[PancakeSwapImage](LiquidityPanacakeSwap.PNG)

Here is the liquidity of Goerli and RTK that shows the price of RTK for each Goerli coin
[GoerliLiquidity](C:/Users/ritvi/Downloads/LiquidityPanacakeSwap.png)

Once the token is deployed, users can earn Goerli from a faucet and convert that to RTK. Here is what an RTK token looks like on MetaMask.
[RTKtoken](C:/Users/ritvi/Downloads/RTKtoken.png)

We used Solidity, openzepplin, and hardhat to deploy the contract with information as follows:
[RTKDeployment](C:/Users/ritvi/Downloads/RTKDeployment.png)

Here is the deployment script for the RTK Token:
[DeploymentScript](C:/Users/ritvi/Downloads/DeploymentScript.png)

And here is the edited hardhat config code using goerli:
[Config](C:/Users/ritvi/Downloads/ConfigFile.png)
