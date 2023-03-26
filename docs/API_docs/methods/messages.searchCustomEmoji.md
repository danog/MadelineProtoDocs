---
title: "messages.searchCustomEmoji"
description: "messages.searchCustomEmoji parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchCustomEmoji.html
---
# Method: messages.searchCustomEmoji
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emoticon|[string](/API_docs/types/string.html) | Yes|
|hash|Array of [long](/API_docs/types/long.html) | Optional|


### Return type: [EmojiList](/API_docs/types/EmojiList.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EmojiList = $MadelineProto->messages->searchCustomEmoji(emoticon: 'string', hash: [long, long], );
```

