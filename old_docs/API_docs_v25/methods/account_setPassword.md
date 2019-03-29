---
title: account.setPassword
description: Set 2FA password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.setPassword  
[Back to methods index](index.md)


Set 2FA password

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|current\_password\_hash|[bytes](../types/bytes.md) | Use only if you have set a 2FA password: `$current_salt = $MadelineProto->account->getPassword()['current_salt']; $current_password_hash = hash('sha256', $current_salt.$password.$current_salt, true);` | Yes|
|new\_salt|[bytes](../types/bytes.md) | New salt | Yes|
|new\_password\_hash|[bytes](../types/bytes.md) | `hash('sha256', $new_salt.$new_password.$new_salt, true)` | Yes|
|hint|[string](../types/string.md) | Hint | Yes|


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

$Bool = $MadelineProto->account->setPassword(['current_password_hash' => 'bytes', 'new_salt' => 'bytes', 'new_password_hash' => 'bytes', 'hint' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.setPassword({current_password_hash='bytes', new_salt='bytes', new_password_hash='bytes', hint='string', })
```

