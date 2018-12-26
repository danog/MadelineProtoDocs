---
title: recentMeUrlStickerSet
description: Recent me URL sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlStickerSet  
[Back to constructors index](index.md)



Recent me URL sticker set

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|set|[StickerSetCovered](../types/StickerSetCovered.md) | Yes|Set|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlStickerSet = ['_' => 'recentMeUrlStickerSet', 'url' => 'string', 'set' => StickerSetCovered];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "recentMeUrlStickerSet", "url": "string", "set": StickerSetCovered}
```


Or, if you're into Lua:

```lua
recentMeUrlStickerSet={_='recentMeUrlStickerSet', url='string', set=StickerSetCovered}

```


