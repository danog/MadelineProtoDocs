---
title: test.useError
description: test.useError parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/test_useError.html
---
# Method: test.useError
[Back to methods index](index.md)





### Return type: [Error](../types/Error.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Error = $MadelineProto->test->useError();
```

Or, if you're into Lua:

```lua
Error = test.useError({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_METHOD_INVALID_4000689921_X|Invalid method|


