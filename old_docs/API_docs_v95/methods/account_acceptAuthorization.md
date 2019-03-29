---
title: account.acceptAuthorization
description: Accept telegram passport authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.acceptAuthorization  
[Back to methods index](index.md)


Accept telegram passport authorization

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_id|[int](../types/int.md) | Bot ID | Yes|
|scope|[string](../types/string.md) | Scope | Yes|
|public\_key|[string](../types/string.md) | The bot's RSA public key | Yes|
|value\_hashes|Array of [SecureValueHash](../types/SecureValueHash.md) | Hashes of the encrypted credentials | Yes|
|credentials|[SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md) | Encrypted secure credentials | Yes|


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

$Bool = $MadelineProto->account->acceptAuthorization(['bot_id' => int, 'scope' => 'string', 'public_key' => 'string', 'value_hashes' => [SecureValueHash, SecureValueHash], 'credentials' => SecureCredentialsEncrypted, ]);
```

Or, if you're into Lua:

```lua
Bool = account.acceptAuthorization({bot_id=int, scope='string', public_key='string', value_hashes={SecureValueHash}, credentials=SecureCredentialsEncrypted, })
```

