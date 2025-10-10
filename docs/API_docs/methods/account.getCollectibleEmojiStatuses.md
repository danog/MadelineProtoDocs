---
title: "account.getCollectibleEmojiStatuses"
description: "Obtain a list of [emoji statuses »](https://core.telegram.org/api/emoji-status) for owned [collectible gifts](https://core.telegram.org/api/gifts#collectible-gifts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getCollectibleEmojiStatuses.html
---
# Method: account.getCollectibleEmojiStatuses
[Back to methods index](index.html)



Obtain a list of [emoji statuses »](https://core.telegram.org/api/emoji-status) for owned [collectible gifts](https://core.telegram.org/api/gifts#collectible-gifts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash for pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [account.EmojiStatuses](/API_docs/types/account.EmojiStatuses.html)

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

$account_EmojiStatuses = $MadelineProto->account->getCollectibleEmojiStatuses(hash: [$long\|string, $long\|string], );
```

