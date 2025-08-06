---
title: "messages.getOutboxReadDate"
description: "Get the exact read date of one of our messages, sent to a private chat with another user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getOutboxReadDate.html
---
# Method: messages.getOutboxReadDate
[Back to methods index](index.html)



Get the exact read date of one of our messages, sent to a private chat with another user.

Can be only done for private outgoing messages not older than [appConfig.pm\_read\_date\_expire\_period »](https://core.telegram.org/api/config#pm-read-date-expire-period).

If the `peer`'s [userFull](../constructors/userFull.html).`read_dates_private` flag is set, we will not be able to fetch the exact read date of messages we send to them, and a `USER_PRIVACY_RESTRICTED` RPC error will be emitted.  
The exact read date of messages might still be unavailable for other reasons, see [here »](../constructors/globalPrivacySettings.html) for more info.  
To set [userFull](../constructors/userFull.html).`read_dates_private` for ourselves invoke [account.setGlobalPrivacySettings](../methods/account.setGlobalPrivacySettings.html), setting the `settings.hide_read_marks` flag.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The user to whom we sent the message. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | The message ID. | Optional|


### Return type: [OutboxReadDate](/API_docs/types/OutboxReadDate.html)

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

$OutboxReadDate = $MadelineProto->messages->getOutboxReadDate(peer: $InputPeer, msg_id: $int, );
```

