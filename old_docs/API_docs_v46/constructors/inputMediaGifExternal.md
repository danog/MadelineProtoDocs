---
title: inputMediaGifExternal
description: Media gif external
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGifExternal  
[Back to constructors index](index.md)



Media gif external

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|q|[string](../types/string.md) | Yes|Q|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGifExternal = ['_' => 'inputMediaGifExternal', 'url' => 'string', 'q' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaGifExternal", "url": "string", "q": "string"}
```


Or, if you're into Lua:

```lua
inputMediaGifExternal={_='inputMediaGifExternal', url='string', q='string'}

```


