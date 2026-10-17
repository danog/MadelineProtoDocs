---
title: "updateWalletGaslessInfo"
description: "updateWalletGaslessInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWalletGaslessInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|available|[Bool](/API_docs/types/Bool.html) | Optional|
|left|[int](/API_docs/types/int.html) | Yes|
|reset\_at|[int](/API_docs/types/int.html) | Yes|
|min\_amount|[long](/API_docs/types/long.html) | Yes|
|relayer\_address|[string](/API_docs/types/string.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateWalletGaslessInfo = ['_' => 'updateWalletGaslessInfo', 'available' => Bool, 'left' => int, 'reset_at' => int, 'min_amount' => long, 'relayer_address' => 'string'];
```  
