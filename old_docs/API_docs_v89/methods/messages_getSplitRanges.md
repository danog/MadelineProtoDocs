---
title: messages.getSplitRanges
description: Get message ranges to fetch
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getSplitRanges  
[Back to methods index](index.md)


Get message ranges to fetch



### Return type: [Vector\_of\_MessageRange](../types/MessageRange.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_MessageRange = $MadelineProto->messages->getSplitRanges();
```

Or, if you're into Lua:

```lua
Vector_of_MessageRange = messages.getSplitRanges({})
```

