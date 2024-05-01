---
title: "inputClientProxy"
description: "Info about an MTProxy used to connect."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputClientProxy  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an [MTProxy](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation) used to connect.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|address|[string](/API_docs/types/string.html) | Yes|Proxy address|
|port|[int](/API_docs/types/int.html) | Yes|Proxy port|



### Type: [InputClientProxy](/API_docs/types/InputClientProxy.html)


### Example:

```
$inputClientProxy = ['_' => 'inputClientProxy', 'address' => 'string', 'port' => int];
```  
