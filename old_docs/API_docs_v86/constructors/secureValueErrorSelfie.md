---
title: secureValueErrorSelfie
description: Secure value error selfie
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorSelfie  
[Back to constructors index](index.md)



Secure value error selfie

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Text|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorSelfie = ['_' => 'secureValueErrorSelfie', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorSelfie", "type": SecureValueType, "file_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "text": "string"}
```


Or, if you're into Lua:

```lua
secureValueErrorSelfie={_='secureValueErrorSelfie', type=SecureValueType, file_hash='bytes', text='string'}

```


