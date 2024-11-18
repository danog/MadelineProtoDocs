---
title: "messages.requestAppWebView"
description: "Open a [bot mini app](https://core.telegram.org/bots/webapps) from a [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links), sending over user information after user confirmation."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestAppWebView.html
---
# Method: messages.requestAppWebView
[Back to methods index](index.html)



Open a [bot mini app](https://core.telegram.org/bots/webapps) from a [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links), sending over user information after user confirmation.

After calling this method, until the user closes the webview, [messages.prolongWebView](../methods/messages.prolongWebView.html) must be called every 60 seconds.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|write\_allowed|[Bool](/API_docs/types/Bool.html) | Set this flag if the bot is asking permission to send messages to the user as specified in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) docs, and the user agreed. | Optional|
|compact|[Bool](/API_docs/types/Bool.html) |  | Optional|
|fullscreen|[Bool](/API_docs/types/Bool.html) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If the client has clicked on the link in a Telegram chat, pass the chat's peer information; otherwise pass the bot's peer information, instead. | Optional|
|app|[InputBotApp](/API_docs/types/InputBotApp.html) | The app obtained by invoking [messages.getBotApp](../methods/messages.getBotApp.html) as specified in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) docs. | Yes|
|start\_param|[string](/API_docs/types/string.html) | If the `startapp` query string parameter is present in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links), pass it to `start_param`. | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | [Theme parameters »](https://core.telegram.org/api/bots/webapps#theme-parameters) | Optional|
|platform|[string](/API_docs/types/string.html) | Short name of the application; 0-64 English letters, digits, and underscores | Optional|


### Return type: [WebViewResult](/API_docs/types/WebViewResult.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WebViewResult = $MadelineProto->messages->requestAppWebView(write_allowed: $Bool, compact: $Bool, fullscreen: $Bool, peer: $InputPeer, app: $InputBotApp, start_param: 'string', theme_params: $DataJSON, platform: 'string', );
```

