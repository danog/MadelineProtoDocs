# messages.getAttachedStickers

> Get stickers attached to a photo or video

[Back to methods index](index.html)



Get stickers attached to a photo or video

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|media|[InputStickeredMedia](/API_docs/types/InputStickeredMedia.html) | Stickered media | Yes|


### Return type: [Vector\_of\_StickerSetCovered](/API_docs/types/StickerSetCovered.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_StickerSetCovered = $MadelineProto->messages->getAttachedStickers(media: $InputStickeredMedia, );
```
