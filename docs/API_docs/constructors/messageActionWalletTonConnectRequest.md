---
title: "messageActionWalletTonConnectRequest"
description: "messageActionWalletTonConnectRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionWalletTonConnectRequest  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|accepted|[Bool](/API_docs/types/Bool.html) | Optional|
|declined|[Bool](/API_docs/types/Bool.html) | Optional|
|session\_id|[long](/API_docs/types/long.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|
|topic|[string](/API_docs/types/string.html) | Optional|
|trace\_id|[string](/API_docs/types/string.html) | Optional|
|dapp\_name|[string](/API_docs/types/string.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionWalletTonConnectRequest = ['_' => 'messageActionWalletTonConnectRequest', 'accepted' => Bool, 'declined' => Bool, 'session_id' => long, 'expires' => int, 'topic' => 'string', 'trace_id' => 'string', 'dapp_name' => 'string'];
```  
