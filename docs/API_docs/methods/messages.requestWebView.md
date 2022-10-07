---
title: "messages.requestWebView"
description: "Open a [bot web app](https://core.telegram.org/bots/webapps), sending over user information after user confirmation."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestWebView.html
---
# Method: messages.requestWebView
[Back to methods index](index.html)



Open a [bot web app](https://core.telegram.org/bots/webapps), sending over user information after user confirmation.

After calling this method, until the user closes the webview, [messages.prolongWebView](../methods/messages.prolongWebView.html) must be called every 60 seconds.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|from\_bot\_menu|[Bool](/API_docs/types/Bool.html) | Whether the webview was opened by clicking on the bot's [menu button »](https://core.telegram.org/api/bots/menu). | Optional|
|silent|[Bool](/API_docs/types/Bool.html) | Whether the inline message that will be sent by the bot on behalf of the user once the web app interaction is [terminated](../methods/messages.sendWebViewResultMessage.html) should be sent silently (no notifications for the receivers). | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Dialog where the web app is being opened, and where the resulting message will be sent (see the [docs for more info »](https://core.telegram.org/api/bots/webapps)). | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot that owns the [web app](https://core.telegram.org/api/bots/webapps) | Optional|
|url|[string](/API_docs/types/string.html) | [Web app URL](https://core.telegram.org/api/bots/webapps) | Optional|
|start\_param|[string](/API_docs/types/string.html) | If the web app was opened from the attachment menu using a [attachment menu deep link](https://core.telegram.org/api/links#bot-attachment-menu-links), `start_param` should contain the `data` from the `startattach` parameter. | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | Theme parameters for the web app | Optional|
|platform|[string](/API_docs/types/string.html) |  | Yes|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Whether the inline message that will be sent by the bot on behalf of the user once the web app interaction is [terminated](../methods/messages.sendWebViewResultMessage.html) should be sent in reply to this message ID. | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Open the web app as the specified peer, sending the resulting the message as the specified peer. | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$WebViewResult = $MadelineProto->messages->requestWebView(from_bot_menu: Bool, silent: Bool, peer: InputPeer, bot: InputUser, url: 'string', start_param: 'string', theme_params: DataJSON, platform: 'string', reply_to_msg_id: int, send_as: InputPeer, );
```

