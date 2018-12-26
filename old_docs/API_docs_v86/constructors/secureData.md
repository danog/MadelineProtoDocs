---
title: secureData
description: Secure data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureData  
[Back to constructors index](index.md)



Secure data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](../types/bytes.md) | Yes|Data|
|data\_hash|[bytes](../types/bytes.md) | Yes|Data hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [SecureData](../types/SecureData.md)


### Example:

```php
$secureData = ['_' => 'secureData', 'data' => 'bytes', 'data_hash' => 'bytes', 'secret' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureData", "data": {"_": "bytes", "bytes":"base64 encoded bytes"}, "data_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secret": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
secureData={_='secureData', data='bytes', data_hash='bytes', secret='bytes'}

```


