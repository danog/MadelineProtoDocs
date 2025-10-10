---
title: "messages.reportMessagesDelivery"
description: "Used for [Telegram Gateway verification messages »](https://telegram.org/blog/star-messages-gateway-2-0-and-more#save-even-more-on-user-verification): indicate to the server that one or more [message](../constructors/message.html)s were received by the client, if requested by the [message](../constructors/message.html).**report\_delivery\_until\_date** flag or the equivalent flag in [push notifications](https://core.telegram.org/api/push-updates)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reportMessagesDelivery.html
---
# Method: messages.reportMessagesDelivery
[Back to methods index](index.html)



Used for [Telegram Gateway verification messages »](https://telegram.org/blog/star-messages-gateway-2-0-and-more#save-even-more-on-user-verification): indicate to the server that one or more [message](../constructors/message.html)s were received by the client, if requested by the [message](../constructors/message.html).**report\_delivery\_until\_date** flag or the equivalent flag in [push notifications](https://core.telegram.org/api/push-updates).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|push|[Bool](/API_docs/types/Bool.html) | Must be set if the messages were received from a [push notification](https://core.telegram.org/api/push-updates). | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where the messages were received. | Optional|
|id|Array of [int](/API_docs/types/int.html) | The IDs of the received messages. | Yes|


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

$Bool = $MadelineProto->messages->reportMessagesDelivery(push: $Bool, peer: $InputPeer, id: [$int, $int], );
```

