---
title: messages.deleteHistory
description: Delete chat history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.deleteHistory  
[Back to methods index](index.md)


Delete chat history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|just\_clear|[Bool](../types/Bool.md) | Only clear it from your side | Optional|
|revoke|[Bool](../types/Bool.md) | Delete messages for the other user | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to clear it | Optional|
|max\_id|[int](../types/int.md) | Maximum message id of messages to delete | Yes|


### Return type: [messages\_AffectedHistory](../types/messages_AffectedHistory.md)

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

$messages_AffectedHistory = $MadelineProto->messages->deleteHistory(['just_clear' => Bool, 'revoke' => Bool, 'peer' => InputPeer, 'max_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.deleteHistory({just_clear=Bool, revoke=Bool, peer=InputPeer, max_id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


