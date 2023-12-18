---
title: "messages.requestSimpleWebView"
description: "Open a [bot web app](https://core.telegram.org/api/bots/webapps)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestSimpleWebView.html
---
# Method: messages.requestSimpleWebView
[Back to methods index](index.html)



Open a [bot web app](https://core.telegram.org/api/bots/webapps).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|from\_switch\_webview|[Bool](/API_docs/types/Bool.html) | Whether the webapp was opened by clicking on the `switch_webview` button shown on top of the inline results list returned by [messages.getInlineBotResults](../methods/messages.getInlineBotResults.html). | Optional|
|from\_side\_menu|[Bool](/API_docs/types/Bool.html) |  | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Bot that owns the webapp | Optional|
|url|[string](/API_docs/types/string.html) | Web app URL | Optional|
|start\_param|[string](/API_docs/types/string.html) |  | Optional|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | [Theme parameters »](https://core.telegram.org/api/bots/webapps#theme-parameters) | Optional|
|platform|[string](/API_docs/types/string.html) | Short name of the application; 0-64 English letters, digits, and underscores | Optional|


### Return type: [SimpleWebViewResult](/API_docs/types/SimpleWebViewResult.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$SimpleWebViewResult = $MadelineProto->messages->requestSimpleWebView(from_switch_webview: $Bool, from_side_menu: $Bool, bot: $InputUser, url: 'string', start_param: 'string', theme_params: $DataJSON, platform: 'string', );
```

