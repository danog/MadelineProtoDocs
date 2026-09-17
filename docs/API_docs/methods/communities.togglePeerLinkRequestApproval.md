---
title: "communities.togglePeerLinkRequestApproval"
description: "communities.togglePeerLinkRequestApproval parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/communities_togglePeerLinkRequestApproval.html
---
# Method: communities.togglePeerLinkRequestApproval
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reject|[Bool](/API_docs/types/Bool.html) | Optional|
|community|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|


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

$Bool = $MadelineProto->communities->togglePeerLinkRequestApproval(reject: $Bool, community: $InputChannel, peer: $InputPeer, );
```

