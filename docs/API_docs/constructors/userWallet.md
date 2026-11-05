---
title: "userWallet"
description: "userWallet attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userWallet  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|address|[string](/API_docs/types/string.html) | Yes|
|balance|[long](/API_docs/types/long.html) | Yes|
|public\_key|[bytes](/API_docs/types/bytes.html) | Optional|
|state\_init|[bytes](/API_docs/types/bytes.html) | Optional|



### Type: [UserWallet](/API_docs/types/UserWallet.html)


### Example:

```
$userWallet = ['_' => 'userWallet', 'address' => 'string', 'balance' => long, 'public_key' => 'bytes', 'state_init' => 'bytes'];
```  
