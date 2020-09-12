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
|offset|[int](../types/int.md) |  | Yes|
|max\_id|[int](../types/int.md) |  | Yes|
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

$messages.Dialogs = $MadelineProto->messages->getDialogs(['offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Dialogs = messages.getDialogs({offset=int, max_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_INVALID|Invalid folder ID|
|400|INPUT_CONSTRUCTOR_INVALID|The provided constructor is invalid|
|400|OFFSET_PEER_ID_INVALID|The provided offset peer is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


