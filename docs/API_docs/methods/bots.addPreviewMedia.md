---
title: "bots.addPreviewMedia"
description: "bots.addPreviewMedia parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_addPreviewMedia.html
---
# Method: bots.addPreviewMedia
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|lang\_code|[string](/API_docs/types/string.html) | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Optional|


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

