---
title: help.getSupport
description: Returns the support user for the 'ask a question' feature.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getSupport  
[Back to methods index](index.md)


Returns the support user for the 'ask a question' feature.



### Return type: [help.Support](../types/help.Support.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.Support = $MadelineProto->help->getSupport();
```

Or, if you're into Lua:

```lua
help.Support = help.getSupport({})
```

