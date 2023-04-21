---
title: "bots.reorderUsernames"
description: "bots.reorderUsernames parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_reorderUsernames.html
---
# Method: bots.reorderUsernames
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|order|Array of [string](/API_docs/types/string.html) | Yes|


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

$Bool = $MadelineProto->bots->reorderUsernames(bot: InputUser, order: ['string', 'string'], );
```

