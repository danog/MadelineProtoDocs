---
title: "messages.requestWebView"
description: "messages.requestWebView parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestWebView.html
---
# Method: messages.requestWebView
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_bot\_menu|[Bool](/API_docs/types/Bool.html) | Optional|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|url|[string](/API_docs/types/string.html) | Optional|
|start\_param|[string](/API_docs/types/string.html) | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$WebViewResult = $MadelineProto->messages->requestWebView(from_bot_menu: Bool, silent: Bool, peer: InputPeer, bot: InputUser, url: 'string', start_param: 'string', theme_params: DataJSON, reply_to_msg_id: int, send_as: InputPeer, );
```

