---
title: "channels.updateEmojiStatus"
description: "channels.updateEmojiStatus parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_updateEmojiStatus.html
---
# Method: channels.updateEmojiStatus
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Optional|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


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

