---
title: account.resetWebAuthorizations
description: Reset all active web [telegram login](https://core.telegram.org/widgets/login) sessions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resetWebAuthorizations  
[Back to methods index](index.md)


Reset all active web [telegram login](https://core.telegram.org/widgets/login) sessions



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

$Bool = $MadelineProto->account->resetWebAuthorizations();
```

Or, if you're into Lua:

```lua
Bool = account.resetWebAuthorizations({})
```

