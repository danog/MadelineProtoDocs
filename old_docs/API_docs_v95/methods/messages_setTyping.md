---
title: messages.setTyping
description: Change typing status
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setTyping  
[Back to methods index](index.md)


Change typing status

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to change typing status | Optional|
|action|[SendMessageAction](../types/SendMessageAction.md) | Typing status | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setTyping(['peer' => InputPeer, 'action' => SendMessageAction, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setTyping({peer=InputPeer, action=SendMessageAction, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|CHAT_ID_INVALID|The provided chat id is invalid|
|PEER_ID_INVALID|The provided peer id is invalid|
|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|USER_IS_BLOCKED|User is blocked|
|USER_IS_BOT|Bots can't send messages to other bots|
|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


