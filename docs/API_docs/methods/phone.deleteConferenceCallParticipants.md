---
title: "phone.deleteConferenceCallParticipants"
description: "Remove participants from a conference call."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_deleteConferenceCallParticipants.html
---
# Method: phone.deleteConferenceCallParticipants
[Back to methods index](index.html)



Remove participants from a conference call.

Exactly one of the `only_left` and `kick` flags must be set.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|only\_left|[Bool](/API_docs/types/Bool.html) | Whether this is a removal of members that already left the conference call. | Optional|
|kick|[Bool](/API_docs/types/Bool.html) | Whether this is a forced removal of active members in a conference call. | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The conference call. | Yes|
|ids|Array of [long](/API_docs/types/long.html) | IDs of users to remove. | Yes|
|block|[bytes](/API_docs/types/bytes.html) | The [block containing an appropriate e2e.chain.changeSetGroupState event](https://core.telegram.org/api/end-to-end/group-calls) | Yes|


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

$Updates = $MadelineProto->phone->deleteConferenceCallParticipants(only_left: $Bool, kick: $Bool, call: $InputGroupCall, ids: [$long, $long], block: 'bytes', );
```

