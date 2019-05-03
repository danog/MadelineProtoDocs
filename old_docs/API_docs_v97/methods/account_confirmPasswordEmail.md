---
title: account.confirmPasswordEmail
description: Confirm password recovery using email
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.confirmPasswordEmail  
[Back to methods index](index.md)


Confirm password recovery using email

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](../types/string.md) | Code | Yes|


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

$Bool = $MadelineProto->account->confirmPasswordEmail(['code' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.confirmPasswordEmail({code='string', })
```

