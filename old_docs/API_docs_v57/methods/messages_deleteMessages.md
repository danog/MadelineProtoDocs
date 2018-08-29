---
title: messages.deleteMessages
description: Delete messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.deleteMessages  
[Back to methods index](index.md)


Delete messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [int](../types/int.md) | IDs of messages to delete, use channels->deleteMessages for supergroups | Yes|


### Return type: [messages\_AffectedMessages](../types/messages_AffectedMessages.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedMessages = $MadelineProto->messages->deleteMessages(['id' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.deleteMessages
* params - `{"id": [int], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.deleteMessages`

Parameters:

id - Json encoded  array of int




Or, if you're into Lua:

```
messages_AffectedMessages = messages.deleteMessages({id={int}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MESSAGE_DELETE_FORBIDDEN|You can't delete one of the messages you tried to delete, most likely because it is a service message.|


