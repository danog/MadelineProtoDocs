---
title: "bots.getPreviewInfo"
description: "Bot owners only, fetch [main mini app preview information, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_getPreviewInfo.html
---
# Method: bots.getPreviewInfo
[Back to methods index](index.html)



Bot owners only, fetch [main mini app preview information, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info.

Note: technically non-owners may also invoke this method, but it will always behave exactly as [bots.getPreviewMedias](../methods/bots.getPreviewMedias.html), returning only previews for the current language and an empty `lang_codes` array, regardless of the passed `lang_code`, so please only use [bots.getPreviewMedias](../methods/bots.getPreviewMedias.html) if you're not the owner of the `bot`.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot that owns the Main Mini App. | Optional|
|lang\_code|[string](/API_docs/types/string.html) | Fetch previews for the specified ISO 639-1 language code. | Optional|


### Return type: [bots.PreviewInfo](/API_docs/types/bots.PreviewInfo.html)

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

$bots_PreviewInfo = $MadelineProto->bots->getPreviewInfo(bot: $InputUser, lang_code: 'string', );
```

