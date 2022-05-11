---
title: "messages.requestSimpleWebView"
description: "messages.requestSimpleWebView parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestSimpleWebView.html
---
# Method: messages.requestSimpleWebView
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|url|[string](/API_docs/types/string.html) | Yes|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|


### Return type: [SimpleWebViewResult](/API_docs/types/SimpleWebViewResult.html)

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
$SimpleWebViewResult = $MadelineProto->messages->requestSimpleWebView(bot: InputUser, url: 'string', theme_params: DataJSON, );
```

