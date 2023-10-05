---
title: "bots.invokeWebViewCustomMethod"
description: "bots.invokeWebViewCustomMethod parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_invokeWebViewCustomMethod.html
---
# Method: bots.invokeWebViewCustomMethod
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|custom\_method|[string](/API_docs/types/string.html) | Yes|
|params|[DataJSON](/API_docs/types/DataJSON.html) | Yes|


### Return type: [DataJSON](/API_docs/types/DataJSON.html)

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

