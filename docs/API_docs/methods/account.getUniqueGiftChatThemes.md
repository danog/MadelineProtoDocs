---
title: "account.getUniqueGiftChatThemes"
description: "Obtain all [chat themes »](https://core.telegram.org/api/themes#chat-themes) associated to owned [collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getUniqueGiftChatThemes.html
---
# Method: account.getUniqueGiftChatThemes
[Back to methods index](index.html)



Obtain all [chat themes »](https://core.telegram.org/api/themes#chat-themes) associated to owned [collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[string](/API_docs/types/string.html) |  | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Hash from a previously returned [account.chatThemes](../constructors/account.chatThemes.html) constructor, to avoid returning any result if the theme list hasn't changed. | Optional|


### Return type: [account.ChatThemes](/API_docs/types/account.ChatThemes.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_ChatThemes = $MadelineProto->account->getUniqueGiftChatThemes(offset: 'string', limit: $int, hash: [$long\|string, $long\|string], );
```

