---
title: "account.getPaidMessagesRevenue"
description: "Get the number of stars we have received from the specified user thanks to [paid messages »](https://core.telegram.org/api/paid-messages); the received amount will be equal to the sent amount multiplied by [stars\_paid\_message\_commission\_permille](https://core.telegram.org/api/config#stars-paid-message-commission-permille) divided by 1000."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getPaidMessagesRevenue.html
---
# Method: account.getPaidMessagesRevenue
[Back to methods index](index.html)



Get the number of stars we have received from the specified user thanks to [paid messages »](https://core.telegram.org/api/paid-messages); the received amount will be equal to the sent amount multiplied by [stars\_paid\_message\_commission\_permille](https://core.telegram.org/api/config#stars-paid-message-commission-permille) divided by 1000.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, can contain the ID of a [monoforum (channel direct messages)](https://core.telegram.org/api/monoforum) to obtain the number of stars the user has spent to send us direct messages via the channel. | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user that paid to send us messages. | Optional|


### Return type: [account.PaidMessagesRevenue](/API_docs/types/account.PaidMessagesRevenue.html)

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

$account_PaidMessagesRevenue = $MadelineProto->account->getPaidMessagesRevenue(parent_peer: $InputPeer, user_id: $InputUser, );
```

