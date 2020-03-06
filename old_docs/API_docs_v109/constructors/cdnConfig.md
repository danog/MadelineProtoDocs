---
title: cdnConfig
description: Configuration for [CDN](https://core.telegram.org/cdn) file downloads.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnConfig  
[Back to constructors index](index.md)



Configuration for [CDN](https://core.telegram.org/cdn) file downloads.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|public\_keys|Array of [CdnPublicKey](../types/CdnPublicKey.md) | Yes|Public keys|



### Type: [CdnConfig](../types/CdnConfig.md)


### Example:

```php
$cdnConfig = ['_' => 'cdnConfig', 'public_keys' => [CdnPublicKey, CdnPublicKey]];
```  


Or, if you're into Lua:

```lua
cdnConfig={_='cdnConfig', public_keys={CdnPublicKey}}

```


