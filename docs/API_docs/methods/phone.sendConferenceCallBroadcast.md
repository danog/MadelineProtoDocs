---
title: "phone.sendConferenceCallBroadcast"
description: "Broadcast a blockchain block to all members of a conference call, see [here »](https://core.telegram.org/api/end-to-end/group-calls) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_sendConferenceCallBroadcast.html
---
# Method: phone.sendConferenceCallBroadcast
[Back to methods index](index.html)



Broadcast a blockchain block to all members of a conference call, see [here »](https://core.telegram.org/api/end-to-end/group-calls) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The conference where to broadcast the block. | Yes|
|block|[bytes](/API_docs/types/bytes.html) | The block to broadcast. | Yes|


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

$Updates = $MadelineProto->phone->sendConferenceCallBroadcast(call: $InputGroupCall, block: 'bytes', );
```

