---
title: "bots.setBotMenuButton"
description: "Sets the [menu button action »](https://core.telegram.org/api/bots/menu) for a given user or for all users"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_setBotMenuButton.html
---
# Method: bots.setBotMenuButton
[Back to methods index](index.html)



Sets the [menu button action »](https://core.telegram.org/api/bots/menu) for a given user or for all users

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | User ID | Optional|
|button|[BotMenuButton](/API_docs/types/BotMenuButton.html) | Bot menu button action | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->setBotMenuButton(user_id: InputUser, button: BotMenuButton, );
```

