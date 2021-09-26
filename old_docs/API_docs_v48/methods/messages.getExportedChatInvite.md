---
title: messages.getExportedChatInvite
description: messages.getExportedChatInvite parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getExportedChatInvite.html
---
# Method: messages.getExportedChatInvite
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|link|[string](../types/string.md) | Yes|


### Return type: [messages.ExportedChatInvite](../types/messages.ExportedChatInvite.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ExportedChatInvite = $MadelineProto->messages->getExportedChatInvite(['peer' => InputPeer, 'link' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages_ExportedChatInvite = messages.getExportedChatInvite({peer=InputPeer, link='string', })
```

