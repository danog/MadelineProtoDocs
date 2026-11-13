# stickers.changeStickerPosition

> Changes the absolute position of a sticker in the set to which it belongs. The sticker set must have been created by the current user/bot.

[Back to methods index](index.html)



Changes the absolute position of a sticker in the set to which it belongs. The sticker set must have been created by the current user/bot.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The sticker | Optional|
|position|[int](/API_docs/types/int.html) | The new position of the sticker, zero-based | Optional|


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

$messages_StickerSet = $MadelineProto->stickers->changeStickerPosition(sticker: $InputDocument, position: $int, );
```
