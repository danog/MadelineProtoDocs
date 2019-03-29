---
title: stickerPack
description: Sticker pack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerPack  
[Back to constructors index](index.md)



Sticker pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](../types/string.md) | Yes|Emoticon|
|documents|Array of [long](../types/long.md) | Yes|Documents|



### Type: [StickerPack](../types/StickerPack.md)


### Example:

```php
$stickerPack = ['_' => 'stickerPack', 'emoticon' => 'string', 'documents' => [long, long]];
```  


Or, if you're into Lua:

```lua
stickerPack={_='stickerPack', emoticon='string', documents={long}}

```


