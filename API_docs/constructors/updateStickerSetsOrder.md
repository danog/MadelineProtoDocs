# updateStickerSetsOrder

> The order of stickersets was changed

[Back to constructors index](/API_docs/constructors/index.html)



The order of stickersets was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](/API_docs/types/Bool.html) | Optional|Whether the updated stickers are mask stickers|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|Whether the updated stickers are custom emoji stickers|
|order|Array of [long](/API_docs/types/long.html) | Yes|New sticker order by sticker ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'masks' => Bool, 'emojis' => Bool, 'order' => [long, long]];
```
