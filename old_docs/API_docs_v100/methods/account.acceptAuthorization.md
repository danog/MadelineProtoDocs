---
title: account.acceptAuthorization
description: Sends a Telegram Passport authorization form, effectively sharing data with the service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_acceptAuthorization.html
---
# Method: account.acceptAuthorization  
[Back to methods index](index.md)


Sends a Telegram Passport authorization form, effectively sharing data with the service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_id|[int](../types/int.md) | Bot ID | Yes|
|scope|[string](../types/string.md) | Telegram Passport element types requested by the service | Yes|
|public\_key|[string](../types/string.md) | Service's public key | Yes|
|value\_hashes|Array of [SecureValueHash](../types/SecureValueHash.md) | Hashes of the encrypted credentials | Yes|
|credentials|[SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md) | Encrypted values | Yes|


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

$Bool = $MadelineProto->account->acceptAuthorization(['bot_id' => int, 'scope' => 'string', 'public_key' => 'string', 'value_hashes' => [SecureValueHash, SecureValueHash], 'credentials' => SecureCredentialsEncrypted, ]);
```

Or, if you're into Lua:

```lua
Bool = account.acceptAuthorization({bot_id=int, scope='string', public_key='string', value_hashes={SecureValueHash}, credentials=SecureCredentialsEncrypted, })
```

