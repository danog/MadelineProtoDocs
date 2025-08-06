---
title: "messages.viewSponsoredMessage"
description: "Mark a specific [sponsored message »](https://core.telegram.org/api/sponsored-messages) as read"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_viewSponsoredMessage.html
---
# Method: messages.viewSponsoredMessage
[Back to methods index](index.html)



Mark a specific [sponsored message »](https://core.telegram.org/api/sponsored-messages) as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|random\_id|[bytes](/API_docs/types/bytes.html) | The ad's unique ID. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->viewSponsoredMessage(random_id: 'bytes', );
```

