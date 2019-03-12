---
title: messages.getMessages
description: Get messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessages  
[Back to methods index](index.md)


Get messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Message ID or InputMessage](../types/InputMessage.md) | The IDs of messages to fetch (only for users and normal groups) | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

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

$messages_Messages = $MadelineProto->messages->getMessages(['id' => [InputMessage, InputMessage], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getMessages
* params - `{"id": [InputMessage], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getMessages`

Parameters:

id - Json encoded  array of InputMessage




Or, if you're into Lua:

```lua
messages_Messages = messages.getMessages({id={InputMessage}, })
```

