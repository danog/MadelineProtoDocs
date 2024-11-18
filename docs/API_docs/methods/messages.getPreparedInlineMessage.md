---
title: "messages.getPreparedInlineMessage"
description: "messages.getPreparedInlineMessage parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPreparedInlineMessage.html
---
# Method: messages.getPreparedInlineMessage
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|id|[string](/API_docs/types/string.html) | Optional|


### Return type: [messages.PreparedInlineMessage](/API_docs/types/messages.PreparedInlineMessage.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_PreparedInlineMessage = $MadelineProto->messages->getPreparedInlineMessage(bot: $InputUser, id: 'string', );
```

