---
title: "inputWalletImported"
description: "inputWalletImported attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWalletImported  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|public\_key|[bytes](/API_docs/types/bytes.html) | Yes|
|anchor\_public\_key|[bytes](/API_docs/types/bytes.html) | Optional|
|proof|[WalletOwnershipProof](/API_docs/types/WalletOwnershipProof.html) | Yes|



### Type: [InputWalletReplacement](/API_docs/types/InputWalletReplacement.html)


### Example:

```
$inputWalletImported = ['_' => 'inputWalletImported', 'public_key' => 'bytes', 'anchor_public_key' => 'bytes', 'proof' => WalletOwnershipProof];
```  
