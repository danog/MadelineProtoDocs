---
title: "bots.toggleUsername"
description: "Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to a bot we own."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_toggleUsername.html
---
# Method: bots.toggleUsername
[Back to methods index](index.html)



Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to a bot we own.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot | Optional|
|username|[string](/API_docs/types/string.html) | Username | Optional|
|active|[Bool](/API_docs/types/Bool.html) | Whether to activate or deactivate it | Yes|


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

$Bool = $MadelineProto->bots->toggleUsername(bot: $InputUser, username: 'string', active: $Bool, );
```

