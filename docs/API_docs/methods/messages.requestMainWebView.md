---
title: "messages.requestMainWebView"
description: "Open a [Main Mini App](https://core.telegram.org/api/bots/webapps#main-mini-apps)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestMainWebView.html
---
# Method: messages.requestMainWebView
[Back to methods index](index.html)



Open a [Main Mini App](https://core.telegram.org/api/bots/webapps#main-mini-apps).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|compact|[Bool](/API_docs/types/Bool.html) | If set, requests to open the mini app in compact mode (as opposed to normal or fullscreen mode). Must be set if the `mode` parameter of the [Main Mini App link](https://core.telegram.org/api/links#main-mini-app-links) is equal to `compact`. | Optional|
|fullscreen|[Bool](/API_docs/types/Bool.html) | If set, requests to open the mini app in fullscreen mode (as opposed to compact or normal mode). Must be set if the `mode` parameter of the [Main Mini App link](https://core.telegram.org/api/links#main-mini-app-links) is equal to `fullscreen`. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Currently open chat, may be [inputPeerEmpty](../constructors/inputPeerEmpty.html) if no chat is currently open. | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot that owns the main mini app. | Optional|
|start\_param|[string](/API_docs/types/string.html) | Start parameter, if opening from a [Main Mini App link »](https://core.telegram.org/api/links#main-mini-app-links). | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | [Theme parameters »](https://core.telegram.org/api/bots/webapps#theme-parameters) | Optional|
|platform|[string](/API_docs/types/string.html) | Short name of the application; 0-64 English letters, digits, and underscores | Optional|


### Return type: [WebViewResult](/API_docs/types/WebViewResult.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WebViewResult = $MadelineProto->messages->requestMainWebView(compact: $Bool, fullscreen: $Bool, peer: $InputPeer, bot: $InputUser, start_param: 'string', theme_params: $DataJSON, platform: 'string', );
```

