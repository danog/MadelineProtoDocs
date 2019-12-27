---
title: messages.clearRecentStickers
description: Clear recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.clearRecentStickers  
[Back to methods index](index.md)


Clear recent stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](../types/Bool.md) | Set this flag to clear the list of stickers recently attached to photo or video files | Optional|


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

$Bool = $MadelineProto->messages->clearRecentStickers(['attached' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.clearRecentStickers({attached=Bool, })
```

