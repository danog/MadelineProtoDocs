---
title: "wallet.userAddresses"
description: "wallet.userAddresses attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_userAddresses.html
---
# Constructor: wallet.userAddresses  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|addresses|Array of [WalletUserAddress](/API_docs/types/WalletUserAddress.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [wallet.UserAddresses](/API_docs/types/wallet.UserAddresses.html)


### Example:

```
$wallet_userAddresses = ['_' => 'wallet.userAddresses', 'addresses' => [WalletUserAddress, WalletUserAddress], 'users' => [User, User]];
```  
