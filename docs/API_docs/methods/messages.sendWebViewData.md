---
title: "messages.sendWebViewData"
description: "Used by the user to relay data from an opened [reply keyboard bot mini app](https://core.telegram.org/api/bots/webapps) to the bot that owns it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendWebViewData.html
---
# Method: messages.sendWebViewData
[Back to methods index](index.html)



Used by the user to relay data from an opened [reply keyboard bot mini app](https://core.telegram.org/api/bots/webapps) to the bot that owns it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot that owns the web app | Optional|
|button\_text|[string](/API_docs/types/string.html) | Text of the [keyboardButtonSimpleWebView](../constructors/keyboardButtonSimpleWebView.html) that was pressed to open the web app. | Optional|
|data|[string](/API_docs/types/string.html) | Data to relay to the bot, obtained from a [`web_app_data_send` JS event](https://core.telegram.org/api/web-events#web-app-data-send). | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendWebViewData(bot: $InputUser, button_text: 'string', data: 'string', );
```

