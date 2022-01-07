---
title: requestCall
description: requestCall parameters, return type and example
redirect_from: /requestCall.html
grand_parent: "Telegram RPC API"
parent: "Methods"
---
## Method: requestCall  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|id| A username, a bot API chat id, a tg-cli chat id, a [User](API_docs/types/User.html), an [InputPeer](API_docs/types/InputPeer.html), an [InputUser](API_docs/types/InputUser.html), a [Peer](API_docs/types/Peer.html)|

### Return type: [\danog\MadelineProto\VoIP object](https://docs.madelineproto.xyz/API_docs/types/PhoneCall.html)

Returns the call

### Example:


```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();


if (!file_exists('input.raw')) {
    echo 'Downloading example song'.PHP_EOL;
    copy('https://github.com/danog/MadelineProto/raw/master/input.raw', 'input.raw');
}
$call = $MadelineProto->requestCall('@danogentili');
$call->play('input.raw')->then('input.raw')->playOnHold(['input.raw'])->setOutputFile('output.raw');
```

