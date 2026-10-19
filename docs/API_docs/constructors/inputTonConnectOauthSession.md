---
title: "inputTonConnectOauthSession"
description: "inputTonConnectOauthSession attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputTonConnectOauthSession  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|session\_id|[long](/API_docs/types/long.html) | Yes|
|challenge\_answer|[bytes](/API_docs/types/bytes.html) | Yes|
|body|[bytes](/API_docs/types/bytes.html) | Yes|
|proof|[WalletOwnershipProof](/API_docs/types/WalletOwnershipProof.html) | Yes|



### Type: [InputTonConnectOauthSession](/API_docs/types/InputTonConnectOauthSession.html)


### Example:

```
$inputTonConnectOauthSession = ['_' => 'inputTonConnectOauthSession', 'session_id' => long, 'challenge_answer' => 'bytes', 'body' => 'bytes', 'proof' => WalletOwnershipProof];
```  
