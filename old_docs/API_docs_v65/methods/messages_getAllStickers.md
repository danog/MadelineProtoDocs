---
title: messages.getAllStickers
description: Get all stickerpacks
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getAllStickers  
[Back to methods index](index.md)


Get all stickerpacks

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  | Optional|


### Return type: [messages\_AllStickers](../types/messages_AllStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AllStickers = $MadelineProto->messages->getAllStickers(['hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getAllStickers`

Parameters:

hash - Json encoded  array of int




Or, if you're into Lua:

```
messages_AllStickers = messages.getAllStickers({hash={int}, })
```

