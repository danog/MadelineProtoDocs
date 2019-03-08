---
title: secureValueError
description: Secure value error
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueError  
[Back to constructors index](index.md)



Secure value error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|hash|[bytes](../types/bytes.md) | Yes|Hash|
|text|[string](../types/string.md) | Yes|Text|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueError = ['_' => 'secureValueError', 'type' => SecureValueType, 'hash' => 'bytes', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueError", "type": SecureValueType, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "text": "string"}
```


Or, if you're into Lua:

```lua
secureValueError={_='secureValueError', type=SecureValueType, hash='bytes', text='string'}

```


