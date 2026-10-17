---
title: "tonConnectSession"
description: "tonConnectSession attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: tonConnectSession  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|closing|[Bool](/API_docs/types/Bool.html) | Optional|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|dapp\_client\_id|[string](/API_docs/types/string.html) | Yes|
|client\_id|[string](/API_docs/types/string.html) | Optional|
|nonce|[bytes](/API_docs/types/bytes.html) | Yes|
|manifest|[TonConnectManifest](/API_docs/types/TonConnectManifest.html) | Optional|
|manifest\_error|[int](/API_docs/types/int.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|



### Type: [TonConnectSession](/API_docs/types/TonConnectSession.html)


### Example:

```
$tonConnectSession = ['_' => 'tonConnectSession', 'pending' => Bool, 'closing' => Bool, 'closed' => Bool, 'id' => long, 'dapp_client_id' => 'string', 'client_id' => 'string', 'nonce' => 'bytes', 'manifest' => TonConnectManifest, 'manifest_error' => int, 'date' => int];
```  
