---
title: account.setPassword
description: account.setPassword parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setPassword.html
---
# Method: account.setPassword
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|current\_password\_hash|[bytes](../types/bytes.md) | Yes|
|new\_salt|[bytes](../types/bytes.md) | Yes|
|new\_password\_hash|[bytes](../types/bytes.md) | Yes|
|hint|[string](../types/string.md) | Yes|


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

$Bool = $MadelineProto->account->setPassword(['current_password_hash' => 'bytes', 'new_salt' => 'bytes', 'new_password_hash' => 'bytes', 'hint' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.setPassword({current_password_hash='bytes', new_salt='bytes', new_password_hash='bytes', hint='string', })
```

