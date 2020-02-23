---
title: messages.editChatAbout
description: Edit the description of a [group/supergroup/channel](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatAbout.html
---
# Method: messages.editChatAbout  
[Back to methods index](index.md)


Edit the description of a [group/supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The [group/supergroup/channel](https://core.telegram.org/api/channel). | Optional|
|about|[string](../types/string.md) | The new description | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->editChatAbout(['peer' => InputPeer, 'about' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = messages.editChatAbout({peer=InputPeer, about='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ABOUT_NOT_MODIFIED|About text has not changed|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


