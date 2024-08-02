---
title: "messages.requestMainWebView"
description: "messages.requestMainWebView parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestMainWebView.html
---
# Method: messages.requestMainWebView
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|compact|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|start\_param|[string](/API_docs/types/string.html) | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|
|platform|[string](/API_docs/types/string.html) | Optional|


### Return type: [WebViewResult](/API_docs/types/WebViewResult.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WebViewResult = $MadelineProto->messages->requestMainWebView(compact: $Bool, peer: $InputPeer, bot: $InputUser, start_param: 'string', theme_params: $DataJSON, platform: 'string', );
```

