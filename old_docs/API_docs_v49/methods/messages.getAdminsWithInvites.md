---
title: messages.getAdminsWithInvites
description: messages.getAdminsWithInvites parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAdminsWithInvites.html
---
# Method: messages.getAdminsWithInvites
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|


### Return type: [messages.ChatAdminsWithInvites](../types/messages.ChatAdminsWithInvites.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ChatAdminsWithInvites = $MadelineProto->messages->getAdminsWithInvites(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
messages_ChatAdminsWithInvites = messages.getAdminsWithInvites({peer=InputPeer, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


