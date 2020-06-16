---
title: messages.toggleChatAdmins
description: messages.toggleChatAdmins parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleChatAdmins.html
---
# Method: messages.toggleChatAdmins
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|enabled|[Bool](../types/Bool.md) | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->toggleChatAdmins(['chat_id' => InputPeer, 'enabled' => Bool, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.toggleChatAdmins({chat_id=InputPeer, enabled=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|


