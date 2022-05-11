---
title: "account.updateProfile"
description: "Updates user profile."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateProfile.html
---
# Method: account.updateProfile
[Back to methods index](index.html)



Updates user profile.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|first\_name|[string](/API_docs/types/string.html) | New user first name | Optional|
|last\_name|[string](/API_docs/types/string.html) | New user last name | Optional|
|about|[string](/API_docs/types/string.html) | New bio | Optional|


### Return type: [User](/API_docs/types/User.html)

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
$User = $MadelineProto->account->updateProfile(first_name: 'string', last_name: 'string', about: 'string', );
```

