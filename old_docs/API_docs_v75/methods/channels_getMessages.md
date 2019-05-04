---
title: channels.getMessages
description: Get channel/supergroup messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getMessages  
[Back to methods index](index.md)


Get channel/supergroup messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|id|Array of [Message ID or InputMessage](../types/InputMessage.md) | The message IDs | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->channels->getMessages(['channel' => InputChannel, 'id' => [InputMessage, InputMessage], ]);
```

Or, if you're into Lua:

```lua
messages_Messages = channels.getMessages({channel=InputChannel, id={InputMessage}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|MESSAGE_IDS_EMPTY|No message ids were provided|


