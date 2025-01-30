---
title: "bots.addPreviewMedia"
description: "Add a [main mini app preview, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_addPreviewMedia.html
---
# Method: bots.addPreviewMedia
[Back to methods index](index.html)



Add a [main mini app preview, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info.

Only owners of bots with a configured Main Mini App can use this method, see [see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info on how to check if you can invoke this method.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot that owns the Main Mini App. | Optional|
|lang\_code|[string](/API_docs/types/string.html) | ISO 639-1 language code, indicating the localization of the preview to add. | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | The photo/video preview, uploaded using [messages.uploadMedia](../methods/messages.uploadMedia.html). | Optional|


### Return type: [BotPreviewMedia](/API_docs/types/BotPreviewMedia.html)

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

$BotPreviewMedia = $MadelineProto->bots->addPreviewMedia(bot: $InputUser, lang_code: 'string', media: $InputMedia, );
```

