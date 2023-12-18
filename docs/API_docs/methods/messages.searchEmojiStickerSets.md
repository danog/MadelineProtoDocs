---
title: "messages.searchEmojiStickerSets"
description: "messages.searchEmojiStickerSets parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchEmojiStickerSets.html
---
# Method: messages.searchEmojiStickerSets
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|exclude\_featured|[Bool](/API_docs/types/Bool.html) | Optional|
|q|[string](/API_docs/types/string.html) | Optional|
|hash|Array of [long](/API_docs/types/long.html) | Optional|


### Return type: [messages.FoundStickerSets](/API_docs/types/messages.FoundStickerSets.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FoundStickerSets = $MadelineProto->messages->searchEmojiStickerSets(exclude_featured: $Bool, q: 'string', hash: [$long, $long], );
```

