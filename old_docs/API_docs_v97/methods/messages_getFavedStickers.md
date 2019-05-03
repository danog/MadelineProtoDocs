---
title: messages.getFavedStickers
description: Get favorite stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getFavedStickers  
[Back to methods index](index.md)


Get favorite stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  the hash parameter of the previous result of this method | Optional|


### Return type: [messages\_FavedStickers](../types/messages_FavedStickers.md)

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

$messages_FavedStickers = $MadelineProto->messages->getFavedStickers(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_FavedStickers = messages.getFavedStickers({hash={int}, })
```

