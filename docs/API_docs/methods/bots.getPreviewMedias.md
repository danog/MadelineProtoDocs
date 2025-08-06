---
title: "bots.getPreviewMedias"
description: "Fetch [main mini app previews, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_getPreviewMedias.html
---
# Method: bots.getPreviewMedias
[Back to methods index](index.html)



Fetch [main mini app previews, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot that owns the Main Mini App. | Optional|


### Return type: [Vector\_of\_BotPreviewMedia](/API_docs/types/BotPreviewMedia.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_BotPreviewMedia = $MadelineProto->bots->getPreviewMedias(bot: $InputUser, );
```

