---
title: destroy_auth_key
description: destroy_auth_key parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: destroy\_auth\_key
[Back to methods index](index.md)





### Return type: [DestroyAuthKeyRes](../types/DestroyAuthKeyRes.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$DestroyAuthKeyRes = $MadelineProto->destroy_auth_key();
```

Or, if you're into Lua:

```lua
DestroyAuthKeyRes = destroy_auth_key({})
```

