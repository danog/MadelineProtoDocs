---
title: account.updateStatus
description: Update online status
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.updateStatus  
[Back to methods index](index.md)


Update online status

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offline|[Bool](../types/Bool.md) | True to set the status to offline | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updateStatus(['offline' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.updateStatus`

Parameters:

offline - Json encoded Bool




Or, if you're into Lua:

```lua
Bool = account.updateStatus({offline=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


