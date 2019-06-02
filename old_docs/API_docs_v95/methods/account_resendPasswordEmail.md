---
title: account.resendPasswordEmail
description: Resend password recovery email
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resendPasswordEmail  
[Back to methods index](index.md)


Resend password recovery email



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->resendPasswordEmail();
```

Or, if you're into Lua:

```lua
Bool = account.resendPasswordEmail({})
```

