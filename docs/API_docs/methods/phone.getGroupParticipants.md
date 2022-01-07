---
title: "phone.getGroupParticipants"
description: "phone.getGroupParticipants parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupParticipants.html
---
# Method: phone.getGroupParticipants
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|ids|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Yes|
|sources|Array of [int](/API_docs/types/int.html) | Yes|
|offset|[string](/API_docs/types/string.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Yes|


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

$phone_GroupParticipants = $MadelineProto->phone->getGroupParticipants(['call' => InputGroupCall, 'ids' => [InputPeer, InputPeer], 'sources' => [int, int], 'offset' => 'string', 'limit' => int, ]);
```

