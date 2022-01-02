---
title: "secureValueHash"
description: "Secure value hash"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueHash  
[Back to constructors index](index.md)



Secure value hash

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Secure value type|
|hash|[bytes](../types/bytes.md) | Yes|Hash|



### Type: [SecureValueHash](../types/SecureValueHash.md)


### Example:

```php
$secureValueHash = ['_' => 'secureValueHash', 'type' => SecureValueType, 'hash' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureValueHash={_='secureValueHash', type=SecureValueType, hash='bytes'}

```


