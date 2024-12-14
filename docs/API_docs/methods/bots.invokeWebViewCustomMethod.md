---
title: "bots.invokeWebViewCustomMethod"
description: "Send a custom request from a [mini bot app](https://core.telegram.org/api/bots/webapps), triggered by a [web\_app\_invoke\_custom\_method event »](https://core.telegram.org/api/web-events#web-app-invoke-custom-method)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_invokeWebViewCustomMethod.html
---
# Method: bots.invokeWebViewCustomMethod
[Back to methods index](index.html)



Send a custom request from a [mini bot app](https://core.telegram.org/api/bots/webapps), triggered by a [web\_app\_invoke\_custom\_method event »](https://core.telegram.org/api/web-events#web-app-invoke-custom-method).

The response should be sent using a [custom\_method\_invoked](https://core.telegram.org/api/bots/webapps#custom-method-invoked) event, [see here »](https://core.telegram.org/api/web-events#web-app-invoke-custom-method) for more info on the flow.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Identifier of the bot associated to the [mini bot app](https://core.telegram.org/api/bots/webapps) | Optional|
|custom\_method|[string](/API_docs/types/string.html) | Identifier of the custom method to invoke | Optional|
|params|[DataJSON](/API_docs/types/DataJSON.html) | Method parameters | Yes|


### Return type: [DataJSON](/API_docs/types/DataJSON.html)

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

$DataJSON = $MadelineProto->bots->invokeWebViewCustomMethod(bot: $InputUser, custom_method: 'string', params: $DataJSON, );
```

