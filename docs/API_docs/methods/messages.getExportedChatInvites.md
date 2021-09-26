---
title: messages.getExportedChatInvites
description: messages.getExportedChatInvites parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getExportedChatInvites.html
---
# Method: messages.getExportedChatInvites
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revoked|[Bool](../types/Bool.md) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|admin\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Optional|
|offset\_date|[int](../types/int.md) | Optional|
|offset\_link|[string](../types/string.md) | Optional|
|limit|[int](../types/int.md) | Yes|


### Return type: [messages.ExportedChatInvites](../types/messages.ExportedChatInvites.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ExportedChatInvites = $MadelineProto->messages->getExportedChatInvites(['revoked' => Bool, 'peer' => InputPeer, 'admin_id' => InputUser, 'offset_date' => int, 'offset_link' => 'string', 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_ExportedChatInvites = messages.getExportedChatInvites({revoked=Bool, peer=InputPeer, admin_id=InputUser, offset_date=int, offset_link='string', limit=int, })
```

