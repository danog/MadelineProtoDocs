---
title: account.cancelPasswordEmail
description: Cancel password recovery email
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.cancelPasswordEmail  
[Back to methods index](index.md)


Cancel password recovery email



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->cancelPasswordEmail();
```

Or, if you're using async:

```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = yield $MadelineProto->account->cancelPasswordEmail();
```

Or, if you're into Lua:

```lua
Bool = account.cancelPasswordEmail({})
```

