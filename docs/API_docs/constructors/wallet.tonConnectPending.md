---
title: "wallet.tonConnectPending"
description: "wallet.tonConnectPending attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_tonConnectPending.html
---
# Constructor: wallet.tonConnectPending  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|session|[TonConnectSession](/API_docs/types/TonConnectSession.html) | Yes|
|requests|Array of [TonConnectRequest](/API_docs/types/TonConnectRequest.html) | Yes|



### Type: [wallet.TonConnectPending](/API_docs/types/wallet.TonConnectPending.html)


### Example:

```
$wallet_tonConnectPending = ['_' => 'wallet.tonConnectPending', 'session' => TonConnectSession, 'requests' => [TonConnectRequest, TonConnectRequest]];
```  
