---
title: "bots.reorderUsernames"
description: "Reorder usernames associated to a bot we own."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_reorderUsernames.html
---
# Method: bots.reorderUsernames
[Back to methods index](index.html)



Reorder usernames associated to a bot we own.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot | Optional|
|order|Array of [string](/API_docs/types/string.html) | The new order for active usernames. All active usernames must be specified. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->reorderUsernames(bot: $InputUser, order: ['string', 'string'], );
```

