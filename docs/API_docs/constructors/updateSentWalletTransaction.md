---
title: "updateSentWalletTransaction"
description: "updateSentWalletTransaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateSentWalletTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gasless|[Bool](/API_docs/types/Bool.html) | Optional|
|msg\_hash|[string](/API_docs/types/string.html) | Yes|
|transaction|[WalletTransaction](/API_docs/types/WalletTransaction.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSentWalletTransaction = ['_' => 'updateSentWalletTransaction', 'gasless' => Bool, 'msg_hash' => 'string', 'transaction' => WalletTransaction];
```  
