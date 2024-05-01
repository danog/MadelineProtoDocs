---
title: "account.registerDevice"
description: "Register device to receive [PUSH notifications](https://core.telegram.org/api/push-updates)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_registerDevice.html
---
# Method: account.registerDevice
[Back to methods index](index.html)



Register device to receive [PUSH notifications](https://core.telegram.org/api/push-updates)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_muted|[Bool](/API_docs/types/Bool.html) | Avoid receiving (silent and invisible background) notifications. Useful to save battery. | Optional|
|token\_type|[int](/API_docs/types/int.html) | Device token type, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values. | Optional|
|token|[string](/API_docs/types/string.html) | Device token, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values. | Optional|
|app\_sandbox|[Bool](/API_docs/types/Bool.html) | If [(boolTrue)](../constructors/boolTrue.html) is transmitted, a sandbox-certificate will be used during transmission. | Yes|
|secret|[bytes](/API_docs/types/bytes.html) | For FCM and APNS VoIP, optional encryption key used to encrypt push notifications | Yes|
|other\_uids|Array of [long](/API_docs/types/long.html) | List of user identifiers of other users currently using the client | Yes|


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

$Bool = $MadelineProto->account->registerDevice(no_muted: $Bool, token_type: $int, token: 'string', app_sandbox: $Bool, secret: 'bytes', other_uids: [$long, $long], );
```

