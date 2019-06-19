---
title: messages.toggleChatAdmins
description: Enable all users are admins in normal groups (not supergroups)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.toggleChatAdmins  
[Back to methods index](index.md)


Enable all users are admins in normal groups (not supergroups)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Group ID | Optional|
|enabled|[Bool](../types/Bool.md) | Enable all users are admins | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


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

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_ID_INVALID|The provided chat id is invalid|
|CHAT_NOT_MODIFIED|The pinned message wasn't modified|


