---
title: "bots.updateStarRefProgram"
description: "Create, edit or delete the [affiliate program](https://core.telegram.org/api/bots/referrals) of a bot we own"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_updateStarRefProgram.html
---
# Method: bots.updateStarRefProgram
[Back to methods index](index.html)



Create, edit or delete the [affiliate program](https://core.telegram.org/api/bots/referrals) of a bot we own

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot | Optional|
|commission\_permille|[int](/API_docs/types/int.html) | The permille commission rate: it indicates the share of Telegram Stars received by affiliates for every transaction made by users they referred inside of the bot.  <br>  The minimum and maximum values for this parameter are contained in the [starref\_min\_commission\_permille](https://core.telegram.org/api/config#starref-min-commission-permille) and [starref\_max\_commission\_permille](https://core.telegram.org/api/config#starref-max-commission-permille) client configuration parameters. <br>  Can be `0` to terminate the affiliate program.<br>  Both the duration and the commission may only be raised after creation of the program: to lower them, the program must first be terminated and a new one created. | Optional|
|duration\_months|[int](/API_docs/types/int.html) | Indicates the duration of the affiliate program; if not set, there is no expiration date. | Optional|


### Return type: [StarRefProgram](/API_docs/types/StarRefProgram.html)

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

$StarRefProgram = $MadelineProto->bots->updateStarRefProgram(bot: $InputUser, commission_permille: $int, duration_months: $int, );
```

