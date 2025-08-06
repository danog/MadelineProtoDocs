---
title: "bots.toggleUserEmojiStatusPermission"
description: "Allow or prevent a bot from [changing our emoji status »](https://core.telegram.org/api/emoji-status#setting-an-emoji-status-from-a-bot)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_toggleUserEmojiStatusPermission.html
---
# Method: bots.toggleUserEmojiStatusPermission
[Back to methods index](index.html)



Allow or prevent a bot from [changing our emoji status »](https://core.telegram.org/api/emoji-status#setting-an-emoji-status-from-a-bot)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Whether to allow or prevent the bot from changing our emoji status | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->bots->toggleUserEmojiStatusPermission(bot: $InputUser, enabled: $Bool, );
```

