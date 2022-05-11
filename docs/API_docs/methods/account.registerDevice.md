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
|token\_type|[int](/API_docs/types/int.html) | Device token type.<br>**Possible values**:<br>`1` \- APNS (device token for apple push)<br>`2` \- FCM (firebase token for google firebase)<br>`3` \- MPNS (channel URI for microsoft push)<br>`4` \- Simple push (endpoint for firefox's simple push API)<br>`5` \- Ubuntu phone (token for ubuntu push)<br>`6` \- Blackberry (token for blackberry push)<br>`7` \- Unused<br>`8` \- WNS (windows push)<br>`9` \- APNS VoIP (token for apple push VoIP)<br>`10` \- Web push (web push, see below)<br>`11` \- MPNS VoIP (token for microsoft push VoIP)<br>`12` \- Tizen (token for tizen push)<br><br>For `10` web push, the token must be a JSON-encoded object containing the keys described in [PUSH updates](https://core.telegram.org/api/push-updates) | Yes|
|token|[string](/API_docs/types/string.html) | Device token | Yes|
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

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->account->registerDevice(no_muted: Bool, token_type: int, token: 'string', app_sandbox: Bool, secret: 'bytes', other_uids: [long, long], );
```

