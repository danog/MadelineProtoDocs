---
title: messages.getSplitRanges
description: Get message ranges to fetch
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getSplitRanges  
[Back to methods index](index.md)


Get message ranges to fetch



### Return type: [Vector\_of\_MessageRange](../types/MessageRange.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_MessageRange = $MadelineProto->messages->getSplitRanges();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getSplitRanges
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getSplitRanges`

Parameters:




Or, if you're into Lua:

```lua
Vector_of_MessageRange = messages.getSplitRanges({})
```

