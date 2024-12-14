---
title: "channels.updateEmojiStatus"
description: "Set an [emoji status](https://core.telegram.org/api/emoji-status) for a channel."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_updateEmojiStatus.html
---
# Method: channels.updateEmojiStatus
[Back to methods index](index.html)



Set an [emoji status](https://core.telegram.org/api/emoji-status) for a channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The channel, must have at least [`channel_emoji_status_level_min` boosts](https://core.telegram.org/api/config#channel-emoji-status-level-min). | Optional|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | [Emoji status](https://core.telegram.org/api/emoji-status) to set | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->updateEmojiStatus(channel: $InputChannel, emoji_status: $EmojiStatus, );
```

