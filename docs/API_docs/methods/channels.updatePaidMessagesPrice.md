---
title: "channels.updatePaidMessagesPrice"
description: "channels.updatePaidMessagesPrice parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_updatePaidMessagesPrice.html
---
# Method: channels.updatePaidMessagesPrice
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|broadcast\_messages\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Optional|
|send\_paid\_messages\_stars|[long](/API_docs/types/long.html) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->updatePaidMessagesPrice(broadcast_messages_allowed: $Bool, channel: $InputChannel, send_paid_messages_stars: $long, );
```

