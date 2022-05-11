---
title: "phone.getGroupCallJoinAs"
description: "Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupCallJoinAs.html
---
# Method: phone.getGroupCallJoinAs
[Back to methods index](index.html)



Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The dialog whose group call or livestream we're trying to join | Optional|


### Return type: [phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.html)

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
$phone_JoinAsPeers = $MadelineProto->phone->getGroupCallJoinAs(peer: InputPeer, );
```

