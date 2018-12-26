---
title: inputMediaPhotoExternal
description: Media photo external
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhotoExternal  
[Back to constructors index](index.md)



Media photo external

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|caption|[string](../types/string.md) | Yes|Caption|
|ttl\_seconds|[int](../types/int.md) | Optional|Ttl seconds|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPhotoExternal = ['_' => 'inputMediaPhotoExternal', 'url' => 'string', 'caption' => 'string', 'ttl_seconds' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaPhotoExternal", "url": "string", "caption": "string", "ttl_seconds": int}
```


Or, if you're into Lua:

```lua
inputMediaPhotoExternal={_='inputMediaPhotoExternal', url='string', caption='string', ttl_seconds=int}

```


