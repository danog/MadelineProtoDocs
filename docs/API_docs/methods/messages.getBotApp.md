---
title: "messages.getBotApp"
description: "messages.getBotApp parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getBotApp.html
---
# Method: messages.getBotApp
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|app|[InputBotApp](/API_docs/types/InputBotApp.html) | Yes|
|hash|Array of [long](/API_docs/types/long.html) | Optional|


### Return type: [messages.BotApp](/API_docs/types/messages.BotApp.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotApp = $MadelineProto->messages->getBotApp(app: InputBotApp, hash: [long, long], );
```

