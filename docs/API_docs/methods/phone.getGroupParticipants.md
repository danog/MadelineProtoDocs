---
title: "phone.getGroupParticipants"
description: "Get group call participants"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupParticipants.html
---
# Method: phone.getGroupParticipants
[Back to methods index](index.html)



Get group call participants

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Group call | Yes|
|ids|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If specified, will fetch group participant info about the specified peers | Yes|
|sources|Array of [int](/API_docs/types/int.html) | If specified, will fetch group participant info about the specified WebRTC source IDs | Yes|
|offset|[string](/API_docs/types/string.html) | Offset for results, taken from the `next_offset` field of [phone.groupParticipants](../constructors/phone.groupParticipants.html), initially an empty string. <br>Note: if no more results are available, the method call will return an empty `next_offset`; thus, avoid providing the `next_offset` returned in [phone.groupParticipants](../constructors/phone.groupParticipants.html) if it is empty, to avoid an infinite loop. | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$phone_GroupParticipants = $MadelineProto->phone->getGroupParticipants(call: InputGroupCall, ids: [InputPeer, InputPeer], sources: [int, int], offset: 'string', limit: int, );
```

