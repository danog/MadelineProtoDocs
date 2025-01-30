---
title: "messages.searchCustomEmoji"
description: "Look for [custom emojis](https://core.telegram.org/api/custom-emoji) associated to a UTF8 emoji"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchCustomEmoji.html
---
# Method: messages.searchCustomEmoji
[Back to methods index](index.html)



Look for [custom emojis](https://core.telegram.org/api/custom-emoji) associated to a UTF8 emoji

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|emoticon|[string](/API_docs/types/string.html) | The emoji | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). | Optional|


### Return type: [EmojiList](/API_docs/types/EmojiList.html)

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

$EmojiList = $MadelineProto->messages->searchCustomEmoji(emoticon: 'string', hash: [$long\|string, $long\|string], );
```

