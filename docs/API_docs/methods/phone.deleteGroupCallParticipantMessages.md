---
title: "phone.deleteGroupCallParticipantMessages"
description: "phone.deleteGroupCallParticipantMessages parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_deleteGroupCallParticipantMessages.html
---
# Method: phone.deleteGroupCallParticipantMessages
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|report\_spam|[Bool](/API_docs/types/Bool.html) | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|participant|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->deleteGroupCallParticipantMessages(report_spam: $Bool, call: $InputGroupCall, participant: $InputPeer, );
```

