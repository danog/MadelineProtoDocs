---
title: recentMeUrlStickerSet
description: Recent t.me stickerset installation URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlStickerSet  
[Back to constructors index](index.md)



Recent t.me stickerset installation URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|T.me URL|
|set|[StickerSetCovered](../types/StickerSetCovered.md) | Yes|Stickerset|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlStickerSet = ['_' => 'recentMeUrlStickerSet', 'url' => 'string', 'set' => StickerSetCovered];
```  


Or, if you're into Lua:

```lua
recentMeUrlStickerSet={_='recentMeUrlStickerSet', url='string', set=StickerSetCovered}

```


