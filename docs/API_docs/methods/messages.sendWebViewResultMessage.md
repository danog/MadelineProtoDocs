---
title: "messages.sendWebViewResultMessage"
description: "messages.sendWebViewResultMessage parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendWebViewResultMessage.html
---
# Method: messages.sendWebViewResultMessage
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot\_query\_id|[string](/API_docs/types/string.html) | Yes|
|result|[InputBotInlineResult](/API_docs/types/InputBotInlineResult.html) | Yes|


### Return type: [WebViewMessageSent](/API_docs/types/WebViewMessageSent.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$WebViewMessageSent = $MadelineProto->messages->sendWebViewResultMessage(bot_query_id: 'string', result: InputBotInlineResult, );
```

