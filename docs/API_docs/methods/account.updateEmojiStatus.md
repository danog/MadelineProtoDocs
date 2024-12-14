---
title: "account.updateEmojiStatus"
description: "Set an [emoji status](https://core.telegram.org/api/emoji-status)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateEmojiStatus.html
---
# Method: account.updateEmojiStatus
[Back to methods index](index.html)



Set an [emoji status](https://core.telegram.org/api/emoji-status)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | [Emoji status](https://core.telegram.org/api/emoji-status) to set | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->updateEmojiStatus(emoji_status: $EmojiStatus, );
```

