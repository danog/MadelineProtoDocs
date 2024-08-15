---
title: "account.getDefaultBackgroundEmojis"
description: "Get a set of suggested [custom emoji stickers](https://core.telegram.org/api/custom-emoji) that can be used in an [accent color pattern](https://core.telegram.org/api/colors)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getDefaultBackgroundEmojis.html
---
# Method: account.getDefaultBackgroundEmojis
[Back to methods index](index.html)



Get a set of suggested [custom emoji stickers](https://core.telegram.org/api/custom-emoji) that can be used in an [accent color pattern](https://core.telegram.org/api/colors).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long|string](/API_docs/types/long|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [EmojiList](/API_docs/types/EmojiList.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EmojiList = $MadelineProto->account->getDefaultBackgroundEmojis(hash: [$long|string, $long|string], );
```

