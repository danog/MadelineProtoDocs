---
title: "account.acceptAuthorization"
description: "Sends a Telegram Passport authorization form, effectively sharing data with the service"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_acceptAuthorization.html
---
# Method: account.acceptAuthorization
[Back to methods index](index.html)



Sends a Telegram Passport authorization form, effectively sharing data with the service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_id|[long](/API_docs/types/long.html) | Bot ID | Yes|
|scope|[string](/API_docs/types/string.html) | Telegram Passport element types requested by the service | Yes|
|public\_key|[string](/API_docs/types/string.html) | Service's public key | Yes|
|value\_hashes|Array of [SecureValueHash](/API_docs/types/SecureValueHash.html) | Types of values sent and their hashes | Yes|
|credentials|[SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.html) | Encrypted values | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->account->acceptAuthorization(bot_id: long, scope: 'string', public_key: 'string', value_hashes: [SecureValueHash, SecureValueHash], credentials: SecureCredentialsEncrypted, );
```

