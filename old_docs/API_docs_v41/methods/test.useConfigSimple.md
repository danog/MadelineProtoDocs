---
title: test.useConfigSimple
description: test.useConfigSimple parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/test_useConfigSimple.html
---
# Method: test.useConfigSimple
[Back to methods index](index.md)





### Return type: [help.ConfigSimple](../types/help.ConfigSimple.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_ConfigSimple = $MadelineProto->test->useConfigSimple();
```

Or, if you're into Lua:

```lua
help_ConfigSimple = test.useConfigSimple({})
```

