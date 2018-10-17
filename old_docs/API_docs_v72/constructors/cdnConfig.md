---
title: cdnConfig
description: cdnConfig attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnConfig  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|public\_keys|Array of [CdnPublicKey](../types/CdnPublicKey.md) | Yes|



### Type: [CdnConfig](../types/CdnConfig.md)


### Example:

```php
$cdnConfig = ['_' => 'cdnConfig', 'public_keys' => [CdnPublicKey, CdnPublicKey]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "cdnConfig", "public_keys": [CdnPublicKey]}
```


Or, if you're into Lua:

```lua
cdnConfig={_='cdnConfig', public_keys={CdnPublicKey}}

```


