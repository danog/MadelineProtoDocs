---
title: "channels.getGroupsForDiscussion"
description: "Get all groups that can be used as [discussion groups](https://core.telegram.org/api/discussion)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getGroupsForDiscussion.html
---
# Method: channels.getGroupsForDiscussion
[Back to methods index](index.md)



Get all groups that can be used as [discussion groups](https://core.telegram.org/api/discussion).

Returned [legacy group chats](https://core.telegram.org/api/channel) must be first upgraded to [supergroups](https://core.telegram.org/api/channel) before they can be set as a discussion group.  
To set a returned supergroup as a discussion group, access to its old messages must be enabled using [channels.togglePreHistoryHidden](../methods/channels.togglePreHistoryHidden.md), first.



### Return type: [messages.Chats](../types/messages.Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->channels->getGroupsForDiscussion();
```

Or, if you're into Lua:

```lua
messages_Chats = channels.getGroupsForDiscussion({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


