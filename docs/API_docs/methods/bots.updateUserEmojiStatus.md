---
title: "bots.updateUserEmojiStatus"
description: "Change the emoji status of a user (invoked by bots, see [here »](https://core.telegram.org/api/emoji-status#setting-an-emoji-status-from-a-bot) for more info on the full flow)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_updateUserEmojiStatus.html
---
# Method: bots.updateUserEmojiStatus
[Back to methods index](index.html)



Change the emoji status of a user (invoked by bots, see [here »](https://core.telegram.org/api/emoji-status#setting-an-emoji-status-from-a-bot) for more info on the full flow)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user whose emoji status should be changed | Optional|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | The emoji status | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **NO**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->updateUserEmojiStatus(user_id: $InputUser, emoji_status: $EmojiStatus, );
```

