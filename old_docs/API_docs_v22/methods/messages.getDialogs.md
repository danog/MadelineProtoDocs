---
title: messages.getDialogs
description: Returns the current user dialog list.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDialogs.html
---
# Method: messages.getDialogs
[Back to methods index](index.md)



Returns the current user dialog list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_pinned|[Bool](../types/Bool.md) | Exclude pinned dialogs | Optional|
|offset\_date|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_id|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | [Offset peer for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](../types/int.md) | Number of list elements to be returned | Yes|


### Return type: [messages.Dialogs](../types/messages.Dialogs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Dialogs = $MadelineProto->messages->getDialogs(['exclude_pinned' => Bool, 'offset_date' => int, 'offset_id' => int, 'offset_peer' => InputPeer, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Dialogs = messages.getDialogs({exclude_pinned=Bool, offset_date=int, offset_id=int, offset_peer=InputPeer, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_CONSTRUCTOR_INVALID|The provided constructor is invalid|
|400|OFFSET_PEER_ID_INVALID|The provided offset peer is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


