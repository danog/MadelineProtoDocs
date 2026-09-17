---
title: "messages.requestChatJoinWebView"
description: "messages.requestChatJoinWebView parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestChatJoinWebView.html
---
# Method: messages.requestChatJoinWebView
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|
|platform|[string](/API_docs/types/string.html) | Optional|


### Return type: [WebViewResult](/API_docs/types/WebViewResult.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WebViewResult = $MadelineProto->messages->requestChatJoinWebView(query_id: $long, theme_params: $DataJSON, platform: 'string', );
```

