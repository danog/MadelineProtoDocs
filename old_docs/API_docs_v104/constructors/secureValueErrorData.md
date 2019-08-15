---
title: secureValueErrorData
description: Secure value error data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorData  
[Back to constructors index](index.md)



Secure value error data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|data\_hash|[bytes](../types/bytes.md) | Yes|Data hash|
|field|[string](../types/string.md) | Yes|Field|
|text|[string](../types/string.md) | Yes|Text|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorData = ['_' => 'secureValueErrorData', 'type' => SecureValueType, 'data_hash' => 'bytes', 'field' => 'string', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
secureValueErrorData={_='secureValueErrorData', type=SecureValueType, data_hash='bytes', field='string', text='string'}

```


