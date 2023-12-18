---
title: "account.toggleUsername"
description: "Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to the currently logged-in user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_toggleUsername.html
---
# Method: account.toggleUsername
[Back to methods index](index.html)



Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to the currently logged-in user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](/API_docs/types/string.html) | Username | Optional|
|active|[Bool](/API_docs/types/Bool.html) | Whether to activate or deactivate it | Yes|


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

$Bool = $MadelineProto->account->toggleUsername(username: 'string', active: $Bool, );
```

