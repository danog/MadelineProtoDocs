---
title: "channels.setStickers"
description: "Associate a stickerset to the supergroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_setStickers.html
---
# Method: channels.setStickers
[Back to methods index](index.md)



Associate a stickerset to the supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Supergroup | Optional|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | The stickerset to associate | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->setStickers(['channel' => InputChannel, 'stickerset' => InputStickerSet, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|PARTICIPANTS_TOO_FEW|Not enough participants|
|406|STICKERSET_OWNER_ANONYMOUS|Provided stickerset can't be installed as group stickerset to prevent admin deanonymisation.|


