---
title: account.getSecureValue
description: Get secure value for telegram passport
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getSecureValue  
[Back to methods index](index.md)


Get secure value for telegram passport

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Get telegram passport secure parameters | Yes|


### Return type: [Vector\_of\_SecureValue](../types/SecureValue.md)

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

$Vector_of_SecureValue = $MadelineProto->account->getSecureValue(['types' => [SecureValueType, SecureValueType], ]);
```

Or, if you're into Lua:

```lua
Vector_of_SecureValue = account.getSecureValue({types={SecureValueType}, })
```

