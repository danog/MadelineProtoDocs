---
title: phone.getGroupParticipants
description: phone.getGroupParticipants parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupParticipants.html
---
# Method: phone.getGroupParticipants
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|ids|Array of [Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Yes|
|sources|Array of [int](../types/int.md) | Yes|
|offset|[string](../types/string.md) | Yes|
|limit|[int](../types/int.md) | Yes|


### Return type: [phone.GroupParticipants](../types/phone.GroupParticipants.md)

### Can bots use this method: **YES**


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

Or, if you're into Lua:

```lua
phone_GroupParticipants = phone.getGroupParticipants({call=InputGroupCall, ids={InputPeer}, sources={int}, offset='string', limit=int, })
```

