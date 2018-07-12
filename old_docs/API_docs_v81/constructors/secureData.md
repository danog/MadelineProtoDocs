---
title: secureData
description: secureData attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureData  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|data|[bytes](../types/bytes.md) | Yes|
|data\_hash|[bytes](../types/bytes.md) | Yes|
|secret|[bytes](../types/bytes.md) | Yes|



### Type: [SecureData](../types/SecureData.md)


### Example:

```
$secureData = ['_' => 'secureData', 'data' => 'bytes', 'data_hash' => 'bytes', 'secret' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureData", "data": {"_": "bytes", "bytes":"base64 encoded bytes"}, "data_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secret": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
secureData={_='secureData', data='bytes', data_hash='bytes', secret='bytes'}

```


