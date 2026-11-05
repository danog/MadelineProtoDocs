# stickers.replaceSticker

> Replace a sticker in a [stickerset »](https://core.telegram.org/api/stickers).

[Back to methods index](index.html)



Replace a sticker in a [stickerset »](https://core.telegram.org/api/stickers).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Old sticker document. | Optional|
|new\_sticker|[InputStickerSetItem](/API_docs/types/InputStickerSetItem.html) | New sticker. | Yes|


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

$messages_StickerSet = $MadelineProto->stickers->replaceSticker(sticker: $InputDocument, new_sticker: $InputStickerSetItem, );
```
