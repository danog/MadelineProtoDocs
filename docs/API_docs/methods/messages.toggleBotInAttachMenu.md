---
title: "messages.toggleBotInAttachMenu"
description: "Enable or disable [web bot attachment menu »](https://core.telegram.org/api/bots/attach)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleBotInAttachMenu.html
---
# Method: messages.toggleBotInAttachMenu
[Back to methods index](index.html)



Enable or disable [web bot attachment menu »](https://core.telegram.org/api/bots/attach)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|write\_allowed|[Bool](/API_docs/types/Bool.html) | Whether the user authorizes the bot to write messages to them, if requested by [attachMenuBot](../constructors/attachMenuBot.html).`request_write_access` | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot ID | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Toggle | Yes|


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

$Bool = $MadelineProto->messages->toggleBotInAttachMenu(write_allowed: $Bool, bot: $InputUser, enabled: $Bool, );
```

