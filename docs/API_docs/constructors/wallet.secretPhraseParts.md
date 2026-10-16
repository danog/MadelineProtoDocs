---
title: "wallet.secretPhraseParts"
description: "wallet.secretPhraseParts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_secretPhraseParts.html
---
# Constructor: wallet.secretPhraseParts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|token|[string](/API_docs/types/string.html) | Yes|
|dcs|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [wallet.SecretPhraseParts](/API_docs/types/wallet.SecretPhraseParts.html)


### Example:

```
$wallet_secretPhraseParts = ['_' => 'wallet.secretPhraseParts', 'token' => 'string', 'dcs' => [int, int]];
```  
