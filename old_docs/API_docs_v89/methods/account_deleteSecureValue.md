---
title: account.deleteSecureValue
description: Delete secure telegram passport value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.deleteSecureValue  
[Back to methods index](index.md)


Delete secure telegram passport value

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | The values to delete | Yes|


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

$Bool = $MadelineProto->account->deleteSecureValue(['types' => [SecureValueType, SecureValueType], ]);
```

Or, if you're into Lua:

```lua
Bool = account.deleteSecureValue({types={SecureValueType}, })
```

