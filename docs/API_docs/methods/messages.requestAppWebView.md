---
title: "messages.requestAppWebView"
description: "messages.requestAppWebView parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestAppWebView.html
---
# Method: messages.requestAppWebView
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|write\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|app|[InputBotApp](/API_docs/types/InputBotApp.html) | Yes|
|start\_param|[string](/API_docs/types/string.html) | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|
|platform|[string](/API_docs/types/string.html) | Yes|


### Return type: [AppWebViewResult](/API_docs/types/AppWebViewResult.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$AppWebViewResult = $MadelineProto->messages->requestAppWebView(write_allowed: Bool, peer: InputPeer, app: InputBotApp, start_param: 'string', theme_params: DataJSON, platform: 'string', );
```

