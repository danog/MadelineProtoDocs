---
title: messages.exportChatInvite
description: Export chat invite 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.exportChatInvite  
[Back to methods index](index.md)


Export chat invite 

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Export invite only for this user | Optional|


### Return type: [ExportedChatInvite](../types/ExportedChatInvite.md)

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

$ExportedChatInvite = $MadelineProto->messages->exportChatInvite(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
ExportedChatInvite = messages.exportChatInvite({peer=InputPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_ID_INVALID|The provided chat id is invalid|


