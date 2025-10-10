---
title: "payments.toggleChatStarGiftNotifications"
description: "Enables or disables the reception of notifications every time a [gift »](https://core.telegram.org/api/gifts) is received by the specified channel, can only be invoked by admins with `post_messages` [admin rights](../constructors/chatAdminRights.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_toggleChatStarGiftNotifications.html
---
# Method: payments.toggleChatStarGiftNotifications
[Back to methods index](index.html)



Enables or disables the reception of notifications every time a [gift »](https://core.telegram.org/api/gifts) is received by the specified channel, can only be invoked by admins with `post_messages` [admin rights](../constructors/chatAdminRights.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](/API_docs/types/Bool.html) | Whether to enable or disable reception of notifications in the form of [messageActionStarGiftUnique](../constructors/messageActionStarGiftUnique.html) and [messageActionStarGift](../constructors/messageActionStarGift.html) service messages from the channel. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel for which to receive or not receive notifications. | Optional|


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

$Bool = $MadelineProto->payments->toggleChatStarGiftNotifications(enabled: $Bool, peer: $InputPeer, );
```

