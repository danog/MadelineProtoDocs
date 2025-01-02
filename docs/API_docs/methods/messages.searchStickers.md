---
title: "messages.searchStickers"
description: "messages.searchStickers parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchStickers.html
---
# Method: messages.searchStickers
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|
|q|[string](/API_docs/types/string.html) | Optional|
|emoticon|[string](/API_docs/types/string.html) | Optional|
|lang\_code|Array of [string](/API_docs/types/string.html) | Yes|
|offset|[int](/API_docs/types/int.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [messages.FoundStickers](/API_docs/types/messages.FoundStickers.html)

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

$messages_FoundStickers = $MadelineProto->messages->searchStickers(emojis: $Bool, q: 'string', emoticon: 'string', lang_code: ['string', 'string'], offset: $int, limit: $int, hash: [$long\|string, $long\|string], );
```

