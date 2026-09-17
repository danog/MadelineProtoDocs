---
title: "ephemeral.getWelcomeMessages"
description: "ephemeral.getWelcomeMessages parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/ephemeral_getWelcomeMessages.html
---
# Method: ephemeral.getWelcomeMessages
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [ephemeral.WelcomeMessages](/API_docs/types/ephemeral.WelcomeMessages.html)

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

$ephemeral_WelcomeMessages = $MadelineProto->ephemeral->getWelcomeMessages(peer: $InputPeer, hash: [$long\|string, $long\|string], );
```

