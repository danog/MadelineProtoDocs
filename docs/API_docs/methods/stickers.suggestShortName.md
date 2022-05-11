---
title: "stickers.suggestShortName"
description: "Suggests a short name for a given stickerpack name"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_suggestShortName.html
---
# Method: stickers.suggestShortName
[Back to methods index](index.html)



Suggests a short name for a given stickerpack name

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|title|[string](/API_docs/types/string.html) | Sticker pack name | Yes|


### Return type: [stickers.SuggestedShortName](/API_docs/types/stickers.SuggestedShortName.html)

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
$stickers_SuggestedShortName = $MadelineProto->stickers->suggestShortName(title: 'string', );
```

