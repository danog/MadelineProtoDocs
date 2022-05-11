---
title: "account.getNotifyExceptions"
description: "Returns list of chats with non-default notification settings"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getNotifyExceptions.html
---
# Method: account.getNotifyExceptions
[Back to methods index](index.html)



Returns list of chats with non-default notification settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|compare\_sound|[Bool](/API_docs/types/Bool.html) | If true, chats with non-default sound will also be returned | Optional|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](/API_docs/types/InputNotifyPeer.html) | If specified, only chats of the specified category will be returned | Optional|


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
$Updates = $MadelineProto->account->getNotifyExceptions(compare_sound: Bool, peer: InputNotifyPeer, );
```

