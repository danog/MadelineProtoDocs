---
title: account.deleteSecureValue
description: Delete stored [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_deleteSecureValue.html
---
# Method: account.deleteSecureValue
[Back to methods index](index.md)



Delete stored [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Document types to delete | Yes|


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

$Bool = $MadelineProto->account->deleteSecureValue(['types' => [SecureValueType, SecureValueType], ]);
```

Or, if you're into Lua:

```lua
Bool = account.deleteSecureValue({types={SecureValueType}, })
```

