---
title: "messages.getEmojiStatusGroups"
description: "Represents a list of [emoji categories](https://core.telegram.org/api/custom-emoji#emoji-categories), to be used when selecting custom emojis to set as [custom emoji status](https://core.telegram.org/api)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiStatusGroups.html
---
# Method: messages.getEmojiStatusGroups
[Back to methods index](index.html)



Represents a list of [emoji categories](https://core.telegram.org/api/custom-emoji#emoji-categories), to be used when selecting custom emojis to set as [custom emoji status](https://core.telegram.org/api).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long](/API_docs/types/long.html) |  | Optional|


### Return type: [messages.EmojiGroups](/API_docs/types/messages.EmojiGroups.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_EmojiGroups = $MadelineProto->messages->getEmojiStatusGroups(hash: [long, long], );
```

