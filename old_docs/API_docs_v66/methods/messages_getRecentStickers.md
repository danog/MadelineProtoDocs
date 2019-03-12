---
title: messages.getRecentStickers
description: Get recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getRecentStickers  
[Back to methods index](index.md)


Get recent stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](../types/Bool.md) | Get stickers attached to image? | Optional|
|hash|Array of [int](../types/int.md) | IDs the hash parameter of the previous result of this method | Optional|


### Return type: [messages\_RecentStickers](../types/messages_RecentStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_RecentStickers = $MadelineProto->messages->getRecentStickers(['attached' => Bool, 'hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getRecentStickers`

Parameters:

attached - Json encoded Bool

hash - Json encoded  array of int




Or, if you're into Lua:

```lua
messages_RecentStickers = messages.getRecentStickers({attached=Bool, hash={int}, })
```

