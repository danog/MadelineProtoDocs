---
title: messages.createChannel
description: Create channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.createChannel  
[Back to methods index](index.md)


Create channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|title|[string](../types/string.md) | Channel/supergroup title | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->createChannel(['title' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.createChannel
* params - `{"title": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.createChannel`

Parameters:

title - Json encoded string




Or, if you're into Lua:

```
Updates = messages.createChannel({title='string', })
```

