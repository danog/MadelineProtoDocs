---
title: "messages.getBotApp"
description: "Obtain information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getBotApp.html
---
# Method: messages.getBotApp
[Back to methods index](index.html)



Obtain information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|app|[InputBotApp](/API_docs/types/InputBotApp.html) | Bot app information obtained from a [Direct Mini App deep link »](https://core.telegram.org/api/links#direct-mini-app-links). | Yes|
|hash|Array of [long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.BotApp](/API_docs/types/messages.BotApp.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotApp = $MadelineProto->messages->getBotApp(app: $InputBotApp, hash: [$long, $long], );
```

