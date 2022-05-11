---
title: "account.updateUsername"
description: "Changes username for the current user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateUsername.html
---
# Method: account.updateUsername
[Back to methods index](index.html)



Changes username for the current user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](/API_docs/types/string.html) | username or empty string if username is to be removed<br>Accepted characters: a-z (case-insensitive), 0-9 and underscores.<br>Length: 5-32 characters. | Yes|


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
$User = $MadelineProto->account->updateUsername(username: 'string', );
```

