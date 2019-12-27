---
title: messages.deleteMessages
description: Deletes messages by their identifiers.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteMessages.html
---
# Method: messages.deleteMessages  
[Back to methods index](index.md)


Deletes messages by their identifiers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [int](../types/int.md) | IDs of messages to delete, use channels->deleteMessages for supergroups | Yes|


### Return type: [messages.AffectedMessages](../types/messages.AffectedMessages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.AffectedMessages = $MadelineProto->messages->deleteMessages(['id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.AffectedMessages = messages.deleteMessages({id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|403|MESSAGE_DELETE_FORBIDDEN|You can't delete one of the messages you tried to delete, most likely because it is a service message.|


