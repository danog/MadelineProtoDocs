---
title: "rsa_public_key"
description: "rsa_public_key attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: rsa\_public\_key  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|n|[string](../types/string.md) | Yes|
|e|[string](../types/string.md) | Yes|



### Type: [RSAPublicKey](../types/RSAPublicKey.md)


### Example:

```php
$rsa_public_key = ['_' => 'rsa_public_key', 'n' => 'string', 'e' => 'string'];
```  


Or, if you're into Lua:

```lua
rsa_public_key={_='rsa_public_key', n='string', e='string'}

```


