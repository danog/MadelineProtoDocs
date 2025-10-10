---
title: "bots.setCustomVerification"
description: "Verify a user or chat [on behalf of an organization »](https://core.telegram.org/api/bots/verification)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_setCustomVerification.html
---
# Method: bots.setCustomVerification
[Back to methods index](index.html)



Verify a user or chat [on behalf of an organization »](https://core.telegram.org/api/bots/verification).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](/API_docs/types/Bool.html) | If set, adds the verification; otherwise removes verification. | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Must **not** be set if invoked by a bot, **must** be set to the ID of an owned bot if invoked by a user. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer to verify | Optional|
|custom\_description|[string](/API_docs/types/string.html) | Custom description for the verification, the UTF-8 length limit for this field is contained in [bot\_verification\_description\_length\_limit »](https://core.telegram.org/api/config#bot-verification-description-length-limit). <br>If not set, `Was verified by organization "organization_name"` will be used as description. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->setCustomVerification(enabled: $Bool, bot: $InputUser, peer: $InputPeer, custom_description: 'string', );
```

