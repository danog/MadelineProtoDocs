---
title: "account.disablePeerConnectedBot"
description: "Permanently disconnect a specific chat from all [business bots »](https://core.telegram.org/api/bots/connected-business-bots) (equivalent to specifying it in `recipients.exclude_users` during initial configuration with [account.updateConnectedBot »](../methods/account.updateConnectedBot.html)); to reconnect of a chat disconnected using this method the user must reconnect the entire bot by invoking [account.updateConnectedBot »](../methods/account.updateConnectedBot.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_disablePeerConnectedBot.html
---
# Method: account.disablePeerConnectedBot
[Back to methods index](index.html)



Permanently disconnect a specific chat from all [business bots »](https://core.telegram.org/api/bots/connected-business-bots) (equivalent to specifying it in `recipients.exclude_users` during initial configuration with [account.updateConnectedBot »](../methods/account.updateConnectedBot.html)); to reconnect of a chat disconnected using this method the user must reconnect the entire bot by invoking [account.updateConnectedBot »](../methods/account.updateConnectedBot.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat to disconnect | Optional|


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

$Bool = $MadelineProto->account->disablePeerConnectedBot(peer: $InputPeer, );
```

