---
title: messages.deleteRevokedExportedChatInvites
description: messages.deleteRevokedExportedChatInvites parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteRevokedExportedChatInvites.html
---
# Method: messages.deleteRevokedExportedChatInvites
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|admin\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->deleteRevokedExportedChatInvites(['peer' => InputPeer, 'admin_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.deleteRevokedExportedChatInvites({peer=InputPeer, admin_id=InputUser, })
```

