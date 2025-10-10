---
title: "phone.declineConferenceCallInvite"
description: "Declines a conference call invite."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_declineConferenceCallInvite.html
---
# Method: phone.declineConferenceCallInvite
[Back to methods index](index.html)



Declines a conference call invite.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](/API_docs/types/int.html) | The ID of the [messageActionConferenceCall](../constructors/messageActionConferenceCall.html) to decline. | Optional|


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

$Updates = $MadelineProto->phone->declineConferenceCallInvite(msg_id: $int, );
```

