---
title: "payments.changeStarsSubscription"
description: "Activate or deactivate a [Telegram Star subscription »](https://core.telegram.org/api/invites#paid-invite-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_changeStarsSubscription.html
---
# Method: payments.changeStarsSubscription
[Back to methods index](index.html)



Activate or deactivate a [Telegram Star subscription »](https://core.telegram.org/api/invites#paid-invite-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Always pass [inputPeerSelf](../constructors/inputPeerSelf.html). | Optional|
|subscription\_id|[string](/API_docs/types/string.html) | ID of the subscription. | Optional|
|canceled|[Bool](/API_docs/types/Bool.html) | Whether to cancel or reactivate the subscription. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->payments->changeStarsSubscription(peer: $InputPeer, subscription_id: 'string', canceled: $Bool, );
```

