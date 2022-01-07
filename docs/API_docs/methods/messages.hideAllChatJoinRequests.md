---
title: "messages.hideAllChatJoinRequests"
description: "messages.hideAllChatJoinRequests parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_hideAllChatJoinRequests.html
---
# Method: messages.hideAllChatJoinRequests
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|approved|[Bool](/API_docs/types/Bool.md) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Optional|
|link|[string](/API_docs/types/string.md) | Optional|


### Return type: [Updates](/API_docs/types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->hideAllChatJoinRequests(['approved' => Bool, 'peer' => InputPeer, 'link' => 'string', ]);
```

