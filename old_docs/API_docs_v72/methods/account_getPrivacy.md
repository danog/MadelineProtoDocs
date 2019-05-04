---
title: account.getPrivacy
description: Get privacy settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getPrivacy  
[Back to methods index](index.md)


Get privacy settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|key|[InputPrivacyKey](../types/InputPrivacyKey.md) | Privacy setting key | Yes|


### Return type: [account\_PrivacyRules](../types/account_PrivacyRules.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_PrivacyRules = $MadelineProto->account->getPrivacy(['key' => InputPrivacyKey, ]);
```

Or, if you're into Lua:

```lua
account_PrivacyRules = account.getPrivacy({key=InputPrivacyKey, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PRIVACY_KEY_INVALID|The privacy key is invalid|


