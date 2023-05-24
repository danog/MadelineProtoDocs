---
title: "account.unregisterDevice"
description: "Deletes a device by its token, stops sending PUSH-notifications to it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_unregisterDevice.html
---
# Method: account.unregisterDevice
[Back to methods index](index.html)



Deletes a device by its token, stops sending PUSH-notifications to it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token\_type|[int](/API_docs/types/int.html) | Device token type, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values. | Optional|
|token|[string](/API_docs/types/string.html) | Device token, see [PUSH updates](https://core.telegram.org/api/push-updates#subscribing-to-notifications) for the possible values. | Yes|
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

$Bool = $MadelineProto->account->unregisterDevice(token_type: int, token: 'string', other_uids: [long, long], );
```

