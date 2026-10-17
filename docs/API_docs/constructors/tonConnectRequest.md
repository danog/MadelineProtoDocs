---
title: "tonConnectRequest"
description: "tonConnectRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: tonConnectRequest  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|session\_id|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|body|[bytes](/API_docs/types/bytes.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|
|topic|[string](/API_docs/types/string.html) | Optional|
|trace\_id|[string](/API_docs/types/string.html) | Optional|



### Type: [TonConnectRequest](/API_docs/types/TonConnectRequest.html)


### Example:

```
$tonConnectRequest = ['_' => 'tonConnectRequest', 'session_id' => long, 'msg_id' => int, 'body' => 'bytes', 'expires' => int, 'topic' => 'string', 'trace_id' => 'string'];
```  
