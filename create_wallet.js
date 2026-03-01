const { default: Wallet } = require('ethereumjs-wallet');

const wallet = Wallet.generate();

// 輸出錢包資訊
console.log("==================================================");
console.log("🐱 哩比的加密貨幣錢包");
console.log("==================================================");
console.log("");
console.log("📝 地址 (ETH/ERC20):");
console.log(wallet.getAddressString());
console.log("");
console.log("🔑 私鑰 (請嚴格保密!!!):");
console.log(wallet.getPrivateKeyString());
console.log("");
console.log("⚠️  私鑰非常重要！！！");
console.log("⚠️  誰有私鑰，誰就控制這個錢包！！！");
console.log("⚠️  請把私鑰存放在安全的地方！！！");
console.log("");
console.log("==================================================");
