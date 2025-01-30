---
title: "messages.searchStickers"
description: "Search for stickers using AI-powered keyword search"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchStickers.html
---
# Method: messages.searchStickers
[Back to methods index](index.html)



Search for stickers using AI-powered keyword search

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|emojis|[Bool](/API_docs/types/Bool.html) | If set, returns [custom emoji stickers](https://core.telegram.org/api/custom-emoji) | Optional|
|q|[string](/API_docs/types/string.html) | The search term | Optional|
|emoticon|[string](/API_docs/types/string.html) | Space-separated list of emojis to search for | Optional|
|lang\_code|Array of [string](/API_docs/types/string.html) | List of possible IETF language tags of the user's input language; may be empty if unknown | Yes|
|offset|[int](/API_docs/types/int.html) | [Offset for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). <br>The hash may be generated locally by using the `id`s of the returned or stored sticker [document](../constructors/document.html)s. | Optional|


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

