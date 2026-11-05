# updateStickerSets

> Installed stickersets have changed, the client should refetch them as described in the docs.

[Back to constructors index](/API_docs/constructors/index.html)



Installed stickersets have changed, the client should refetch them as [described in the docs](https://core.telegram.org/api/stickers#installing-stickersets).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](/API_docs/types/Bool.html) | Optional|Whether mask stickersets have changed|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|Whether the list of installed [custom emoji stickersets](https://core.telegram.org/api/custom-emoji) has changed|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStickerSets = ['_' => 'updateStickerSets', 'masks' => Bool, 'emojis' => Bool];
```
