---
title: messages.editChatTitle
description: Edit the title of a normal chat (not supergroup)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.editChatTitle  
[Back to methods index](index.md)


Edit the title of a normal chat (not supergroup)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The ID of the chat | Optional|
|title|[string](../types/string.md) | The new title | Yes|


### Return type: [messages\_StatedMessage](../types/messages_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessage = $MadelineProto->messages->editChatTitle(['chat_id' => InputPeer, 'title' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages_StatedMessage = messages.editChatTitle({chat_id=InputPeer, title='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_TITLE_EMPTY|No chat title provided|


