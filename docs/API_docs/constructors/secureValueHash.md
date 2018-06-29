---
title: secureValueHash
description: secureValueHash attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueHash  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|hash|[bytes](../types/bytes.md) | Yes|



### Type: [SecureValueHash](../types/SecureValueHash.md)


### Example:

```
$secureValueHash = ['_' => 'secureValueHash', 'type' => SecureValueType, 'hash' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueHash", "type": SecureValueType, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
secureValueHash={_='secureValueHash', type=SecureValueType, hash='bytes'}

```


