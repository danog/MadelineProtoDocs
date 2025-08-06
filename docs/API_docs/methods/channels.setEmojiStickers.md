---
title: "channels.setEmojiStickers"
description: "Set a [custom emoji stickerset](https://core.telegram.org/api/custom-emoji) for supergroups. Only usable after reaching at least the [boost level »](https://core.telegram.org/api/boost) specified in the [`group_emoji_stickers_level_min` »](https://core.telegram.org/api/config#group-emoji-stickers-level-min) config parameter."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_setEmojiStickers.html
---
# Method: channels.setEmojiStickers
[Back to methods index](index.html)



Set a [custom emoji stickerset](https://core.telegram.org/api/custom-emoji) for supergroups. Only usable after reaching at least the [boost level »](https://core.telegram.org/api/boost) specified in the [`group_emoji_stickers_level_min` »](https://core.telegram.org/api/config#group-emoji-stickers-level-min) config parameter.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The supergroup | Optional|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | The custom emoji stickerset to associate to the supergroup | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->channels->setEmojiStickers(channel: $InputChannel, stickerset: $InputStickerSet, );
```

