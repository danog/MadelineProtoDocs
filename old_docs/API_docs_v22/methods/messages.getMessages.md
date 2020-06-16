---
title: messages.getMessages
description: Returns the list of messages by their IDs.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessages.html
---
# Method: messages.getMessages
[Back to methods index](index.md)



Returns the list of messages by their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [int](../types/int.md) | Message ID list | Yes|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Messages = $MadelineProto->messages->getMessages(['id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.Messages = messages.getMessages({id={int}, })
```

