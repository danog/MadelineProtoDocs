---
title: messages.migrateChat
description: Convert chat to supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.migrateChat  
[Back to methods index](index.md)


Convert chat to supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat to convert | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->migrateChat(['chat_id' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.migrateChat({chat_id=InputPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_ID_INVALID|The provided chat id is invalid|
|PEER_ID_INVALID|The provided peer id is invalid|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|


