---
title: account.deleteAccount
description: Delete this account
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.deleteAccount  
[Back to methods index](index.md)


Delete this account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reason|[string](../types/string.md) | Why are you going away? :( | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->deleteAccount(['reason' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.deleteAccount({reason='string', })
```

