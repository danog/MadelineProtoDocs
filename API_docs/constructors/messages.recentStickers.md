# messages.recentStickers

> Recently used stickers

[Back to constructors index](/API_docs/constructors/index.html)



Recently used stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.html) | Yes|Emojis associated to stickers|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|Recent stickers|
|dates|Array of [int](/API_docs/types/int.html) | Yes|When was each sticker last used|



### Type: [messages.RecentStickers](/API_docs/types/messages.RecentStickers.html)


### Example:

```
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => long, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```
