---
title: "messages.toggleNoForwards"
description: "Enable or disable [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) on a channel or chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleNoForwards.html
---
# Method: messages.toggleNoForwards
[Back to methods index](index.html)



Enable or disable [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) on a channel or chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat or channel | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Enable or disable content protection | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->toggleNoForwards(peer: InputPeer, enabled: Bool, );
```

