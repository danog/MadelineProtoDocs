---
title: cdnPublicKey
description: Cdn public key
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnPublicKey  
[Back to constructors index](index.md)



Cdn public key

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|public\_key|[string](../types/string.md) | Yes|Public key|



### Type: [CdnPublicKey](../types/CdnPublicKey.md)


### Example:

```php
$cdnPublicKey = ['_' => 'cdnPublicKey', 'dc_id' => int, 'public_key' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "cdnPublicKey", "dc_id": int, "public_key": "string"}
```


Or, if you're into Lua:

```lua
cdnPublicKey={_='cdnPublicKey', dc_id=int, public_key='string'}

```


