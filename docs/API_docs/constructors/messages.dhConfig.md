---
title: "messages.dhConfig"
description: "New set of configuring parameters."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dhConfig.html
---
# Constructor: messages.dhConfig  
[Back to constructors index](/API_docs/constructors/index.html)



New set of configuring parameters.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|g|[int](/API_docs/types/int.html) | Yes|New value **prime**, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|
|p|[bytes](/API_docs/types/bytes.html) | Yes|New value **primitive root**, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|
|version|[int](/API_docs/types/int.html) | Yes|Version of set of parameters|
|random|[bytes](/API_docs/types/bytes.html) | Yes|Random sequence of bytes of assigned length|



### Type: [messages.DhConfig](/API_docs/types/messages.DhConfig.html)


### Example:

```
$messages_dhConfig = ['_' => 'messages.dhConfig', 'g' => int, 'p' => 'bytes', 'version' => int, 'random' => 'bytes'];
```  
