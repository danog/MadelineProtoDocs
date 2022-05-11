---
title: "messages.markDialogUnread"
description: "Manually mark dialog as unread"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_markDialogUnread.html
---
# Method: messages.markDialogUnread
[Back to methods index](index.html)



Manually mark dialog as unread

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|unread|[Bool](/API_docs/types/Bool.html) | Mark as unread/read | Optional|
|peer|[Username, chat ID, Update, Message or InputDialogPeer](/API_docs/types/InputDialogPeer.html) | Dialog | Yes|


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
$Bool = $MadelineProto->messages->markDialogUnread(unread: Bool, peer: InputDialogPeer, );
```

