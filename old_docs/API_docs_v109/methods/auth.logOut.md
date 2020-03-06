---
title: auth.logOut
description: You cannot use this method directly, use the logout method instead (see https://docs.madelineproto.xyz for more info)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_logOut.html
---
# Method: auth.logOut  
[Back to methods index](index.md)


You cannot use this method directly, use the logout method instead (see https://docs.madelineproto.xyz for more info)



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->logOut();
```

Or, if you're into Lua:

```lua
Bool = auth.logOut({})
```

