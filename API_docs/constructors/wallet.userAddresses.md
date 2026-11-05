# wallet.userAddresses

> wallet.userAddresses attributes, type and example

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
