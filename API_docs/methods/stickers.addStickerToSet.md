# stickers.addStickerToSet

> Add a sticker to a stickerset. The sticker set must have been created by the current user/bot.

[Back to methods index](index.html)



Add a sticker to a stickerset. The sticker set must have been created by the current user/bot.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | The stickerset | Optional|
|sticker|[InputStickerSetItem](/API_docs/types/InputStickerSetItem.html) | The sticker | Yes|


### Return type: [messages.StickerSet](/API_docs/types/messages.StickerSet.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StickerSet = $MadelineProto->stickers->addStickerToSet(stickerset: $InputStickerSet, sticker: $InputStickerSetItem, );
```
