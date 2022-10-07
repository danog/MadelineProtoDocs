---
title: "account.deleteAccount"
description: "Delete the user's account from the telegram servers."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_deleteAccount.html
---
# Method: account.deleteAccount
[Back to methods index](index.html)



Delete the user's account from the telegram servers.

Can also be used to delete the account of a user that provided the login code, but forgot the 2FA password and no recovery method is configured, see [here »](https://core.telegram.org/api/srp#password-recovery) for more info on password recovery, and [here »](https://core.telegram.org/api/account-deletion) for more info on account deletion.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reason|[string](/API_docs/types/string.html) | Why is the account being deleted, can be empty | Yes|
|password|[InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html) | [2FA password](https://core.telegram.org/api/srp): this field can be omitted even for accounts with 2FA enabled: in this case account account deletion will be delayed by 7 days [as specified in the docs »](https://core.telegram.org/api/account-deletion) | Optional|


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
$Bool = $MadelineProto->account->deleteAccount(reason: 'string', password: InputCheckPasswordSRP, );
```

