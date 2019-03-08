---
title: messages.getMaskStickers
description: Get masks
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMaskStickers  
[Back to methods index](index.md)


Get masks

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  the hash parameter of the previous result of this method | Optional|


### Return type: [messages\_AllStickers](../types/messages_AllStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AllStickers = $MadelineProto->messages->getMaskStickers(['hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getMaskStickers`

Parameters:

hash - Json encoded  array of int




Or, if you're into Lua:

```lua
messages_AllStickers = messages.getMaskStickers({hash={int}, })
```

