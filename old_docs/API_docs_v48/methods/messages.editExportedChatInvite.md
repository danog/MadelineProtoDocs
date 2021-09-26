---
title: messages.editExportedChatInvite
description: messages.editExportedChatInvite parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editExportedChatInvite.html
---
# Method: messages.editExportedChatInvite
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revoked|[Bool](../types/Bool.md) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|link|[string](../types/string.md) | Yes|
|expire\_date|[int](../types/int.md) | Optional|
|usage\_limit|[int](../types/int.md) | Optional|


### Return type: [messages.ExportedChatInvite](../types/messages.ExportedChatInvite.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ExportedChatInvite = $MadelineProto->messages->editExportedChatInvite(['revoked' => Bool, 'peer' => InputPeer, 'link' => 'string', 'expire_date' => int, 'usage_limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_ExportedChatInvite = messages.editExportedChatInvite({revoked=Bool, peer=InputPeer, link='string', expire_date=int, usage_limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


