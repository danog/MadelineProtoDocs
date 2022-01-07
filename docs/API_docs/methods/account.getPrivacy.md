---
title: "account.getPrivacy"
description: "Get privacy settings of current account"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getPrivacy.html
---
# Method: account.getPrivacy
[Back to methods index](index.md)



Get privacy settings of current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|key|[InputPrivacyKey](../types/InputPrivacyKey.md) | Peer category whose privacy settings should be fetched | Yes|


### Return type: [account.PrivacyRules](../types/account.PrivacyRules.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_PrivacyRules = $MadelineProto->account->getPrivacy(['key' => InputPrivacyKey, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PRIVACY_KEY_INVALID|The privacy key is invalid|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-500|No workers running|Internal error|


