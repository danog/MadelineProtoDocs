# messages.allStickers

> Info about all installed stickers

[Back to constructors index](/API_docs/constructors/index.html)



Info about all installed stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|sets|Array of [StickerSet](/API_docs/types/StickerSet.html) | Yes|All stickersets|



### Type: [messages.AllStickers](/API_docs/types/messages.AllStickers.html)


### Example:

```
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => long, 'sets' => [StickerSet, StickerSet]];
```
