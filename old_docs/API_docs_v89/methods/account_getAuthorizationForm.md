---
title: account.getAuthorizationForm
description: Bots only: get telegram passport authorization form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAuthorizationForm  
[Back to methods index](index.md)


Bots only: get telegram passport authorization form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_id|[int](../types/int.md) | Bot ID | Yes|
|scope|[string](../types/string.md) | Scope | Yes|
|public\_key|[string](../types/string.md) | Bot's public key | Yes|


### Return type: [account\_AuthorizationForm](../types/account_AuthorizationForm.md)

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

$account_AuthorizationForm = $MadelineProto->account->getAuthorizationForm(['bot_id' => int, 'scope' => 'string', 'public_key' => 'string', ]);
```

Or, if you're into Lua:

```lua
account_AuthorizationForm = account.getAuthorizationForm({bot_id=int, scope='string', public_key='string', })
```

