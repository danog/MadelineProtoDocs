---
title: messages.clearRecentStickers
description: Clear recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_clearRecentStickers.html
---
# Method: messages.clearRecentStickers
[Back to methods index](index.md)



Clear recent stickers



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->clearRecentStickers();
```

Or, if you're into Lua:

```lua
Bool = messages.clearRecentStickers({})
```

