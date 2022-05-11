---
title: "phone.saveDefaultGroupCallJoinAs"
description: "Set the default peer that will be used to join a group call in a specific dialog."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_saveDefaultGroupCallJoinAs.html
---
# Method: phone.saveDefaultGroupCallJoinAs
[Back to methods index](index.html)



Set the default peer that will be used to join a group call in a specific dialog.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The dialog | Optional|
|join\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The default peer that will be used to join group calls in this dialog, presenting yourself as a specific user/channel. | Optional|


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
$Bool = $MadelineProto->phone->saveDefaultGroupCallJoinAs(peer: InputPeer, join_as: InputPeer, );
```

