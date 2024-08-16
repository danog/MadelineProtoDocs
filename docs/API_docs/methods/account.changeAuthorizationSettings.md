---
title: "account.changeAuthorizationSettings"
description: "Change settings related to a session."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_changeAuthorizationSettings.html
---
# Method: account.changeAuthorizationSettings
[Back to methods index](index.html)



Change settings related to a session.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|confirmed|[Bool](/API_docs/types/Bool.html) | If set, [confirms a newly logged in session »](https://core.telegram.org/api/auth#confirming-login). | Optional|
|hash|Array of [long\|string](/API_docs/types/long|string.html) | Session ID from the [authorization](../constructors/authorization.html) constructor, fetchable using [account.getAuthorizations](../methods/account.getAuthorizations.html) | Optional|
|encrypted\_requests\_disabled|[Bool](/API_docs/types/Bool.html) | Whether to enable or disable receiving encrypted chats: if the flag is not set, the previous setting is not changed | Optional|
|call\_requests\_disabled|[Bool](/API_docs/types/Bool.html) | Whether to enable or disable receiving calls: if the flag is not set, the previous setting is not changed | Optional|


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

$Bool = $MadelineProto->account->changeAuthorizationSettings(confirmed: $Bool, hash: [$long|string, $long|string], encrypted_requests_disabled: $Bool, call_requests_disabled: $Bool, );
```

