---
title: "messages.discardEncryption"
description: "Cancels a request for creation and/or delete info on secret chat."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_discardEncryption.html
---
# Method: messages.discardEncryption
[Back to methods index](index.md)



Cancels a request for creation and/or delete info on secret chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|delete\_history|[Bool](../types/Bool.md) |  | Optional|
|chat\_id|[int](../types/int.md) | Secret chat ID | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->discardEncryption(['delete_history' => Bool, 'chat_id' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.discardEncryption({delete_history=Bool, chat_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_EMPTY|The provided chat ID is empty|
|400|ENCRYPTION_ALREADY_DECLINED|The secret chat was already declined|
|400|ENCRYPTION_ID_INVALID|The provided secret chat ID is invalid|


