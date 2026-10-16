---
title: "walletState"
description: "walletState attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: walletState  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|backup\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_export\_phrase|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_enable\_backup|[Bool](/API_docs/types/Bool.html) | Optional|
|address|[string](/API_docs/types/string.html) | Yes|
|public\_key|[bytes](/API_docs/types/bytes.html) | Yes|
|balance|[long](/API_docs/types/long.html) | Yes|



### Type: [WalletState](/API_docs/types/WalletState.html)


### Example:

```
$walletState = ['_' => 'walletState', 'backup_enabled' => Bool, 'can_export_phrase' => Bool, 'can_enable_backup' => Bool, 'address' => 'string', 'public_key' => 'bytes', 'balance' => long];
```  
