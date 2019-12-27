---
title: account.saveSecureValue
description: Securely save [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.saveSecureValue  
[Back to methods index](index.md)


Securely save [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|value|[InputSecureValue](../types/InputSecureValue.md) | Secure value, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption) | Yes|
|secure\_secret\_id|[long](../types/long.md) | Passport secret hash, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption) | Yes|


### Return type: [SecureValue](../types/SecureValue.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$SecureValue = $MadelineProto->account->saveSecureValue(['value' => InputSecureValue, 'secure_secret_id' => long, ]);
```

Or, if you're into Lua:

```lua
SecureValue = account.saveSecureValue({value=InputSecureValue, secure_secret_id=long, })
```

