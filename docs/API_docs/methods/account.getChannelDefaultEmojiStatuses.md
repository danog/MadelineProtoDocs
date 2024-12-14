---
title: "account.getChannelDefaultEmojiStatuses"
description: "Get a list of default suggested [channel emoji statuses](https://core.telegram.org/api/emoji-status)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getChannelDefaultEmojiStatuses.html
---
# Method: account.getChannelDefaultEmojiStatuses
[Back to methods index](index.html)



Get a list of default suggested [channel emoji statuses](https://core.telegram.org/api/emoji-status).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [account.EmojiStatuses](/API_docs/types/account.EmojiStatuses.html)

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

$account_EmojiStatuses = $MadelineProto->account->getChannelDefaultEmojiStatuses(hash: [$long\|string, $long\|string], );
```

