---
title: "account.updateConnectedBot"
description: "Connect a [business bot »](https://core.telegram.org/api/business#connected-bots) to the current account, or to change the current connection settings."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateConnectedBot.html
---
# Method: account.updateConnectedBot
[Back to methods index](index.html)



Connect a [business bot »](https://core.telegram.org/api/business#connected-bots) to the current account, or to change the current connection settings.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|deleted|[Bool](/API_docs/types/Bool.html) | Whether to fully disconnect the bot from the current account. | Optional|
|rights|[BusinessBotRights](/API_docs/types/BusinessBotRights.html) |  | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot to connect or disconnect | Optional|
|recipients|[InputBusinessBotRecipients](/API_docs/types/InputBusinessBotRecipients.html) | Configuration for the business connection | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->account->updateConnectedBot(deleted: $Bool, rights: $BusinessBotRights, bot: $InputUser, recipients: $InputBusinessBotRecipients, );
```

