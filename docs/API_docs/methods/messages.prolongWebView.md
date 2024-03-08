---
title: "messages.prolongWebView"
description: "Indicate to the server (from the user side) that the user is still using a web app."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_prolongWebView.html
---
# Method: messages.prolongWebView
[Back to methods index](index.html)



Indicate to the server (from the user side) that the user is still using a web app.

If the method returns a `QUERY_ID_INVALID` error, the webview must be closed.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Whether the inline message that will be sent by the bot on behalf of the user once the web app interaction is [terminated](../methods/messages.sendWebViewResultMessage.html) should be sent silently (no notifications for the receivers). | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Dialog where the web app was opened. | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot that owns the [web app](https://core.telegram.org/api/bots/webapps) | Optional|
|query\_id|[long](/API_docs/types/long.html) | Web app interaction ID obtained from [messages.requestWebView](../methods/messages.requestWebView.html) | Yes|
|reply\_to|[InputReplyTo](/API_docs/types/InputReplyTo.html) | If set, indicates that the inline message that will be sent by the bot on behalf of the user once the web app interaction is [terminated](../methods/messages.sendWebViewResultMessage.html) should be sent in reply to the specified message or story. | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Open the web app as the specified peer | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->prolongWebView(silent: $Bool, peer: $InputPeer, bot: $InputUser, query_id: $long, reply_to: $InputReplyTo, send_as: $InputPeer, );
```

