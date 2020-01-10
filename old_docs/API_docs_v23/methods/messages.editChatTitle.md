---
title: messages.editChatTitle
description: Chanages chat name and sends a service message on it.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatTitle.html
---
# Method: messages.editChatTitle  
[Back to methods index](index.md)


Chanages chat name and sends a service message on it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The ID of the chat | Optional|
|title|[string](../types/string.md) | New chat name, different from the old one | Yes|


### Return type: [messages.StatedMessage](../types/messages.StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.StatedMessage = $MadelineProto->messages->editChatTitle(['chat_id' => InputPeer, 'title' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages.StatedMessage = messages.editChatTitle({chat_id=InputPeer, title='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|CHAT_TITLE_EMPTY|No chat title provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|


