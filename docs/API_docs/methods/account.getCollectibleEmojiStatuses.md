---
title: "account.getCollectibleEmojiStatuses"
description: "account.getCollectibleEmojiStatuses parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getCollectibleEmojiStatuses.html
---
# Method: account.getCollectibleEmojiStatuses
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [account.EmojiStatuses](/API_docs/types/account.EmojiStatuses.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


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

