---
title: "messages.searchStickerSets"
description: "Search for stickersets"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchStickerSets.html
---
# Method: messages.searchStickerSets
[Back to methods index](index.html)



Search for stickersets

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_featured|[Bool](/API_docs/types/Bool.html) | Exclude featured stickersets from results | Optional|
|q|[string](/API_docs/types/string.html) | Query string | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$messages_FoundStickerSets = $MadelineProto->messages->searchStickerSets(exclude_featured: Bool, q: 'string', hash: long, );
```

