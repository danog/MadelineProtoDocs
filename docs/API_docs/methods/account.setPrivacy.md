---
title: "account.setPrivacy"
description: "Change privacy settings of current account"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setPrivacy.html
---
# Method: account.setPrivacy
[Back to methods index](index.html)



Change privacy settings of current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|key|[InputPrivacyKey](/API_docs/types/InputPrivacyKey.html) | Peers to which the privacy rules apply | Yes|
|rules|Array of [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html) | New privacy rules | Yes|


### Return type: [account.PrivacyRules](/API_docs/types/account.PrivacyRules.html)

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
$account_PrivacyRules = $MadelineProto->account->setPrivacy(key: InputPrivacyKey, rules: [InputPrivacyRule, InputPrivacyRule], );
```

