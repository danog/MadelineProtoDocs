---
title: "bots.reorderPreviewMedias"
description: "bots.reorderPreviewMedias parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_reorderPreviewMedias.html
---
# Method: bots.reorderPreviewMedias
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|lang\_code|[string](/API_docs/types/string.html) | Optional|
|order|Array of [MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->reorderPreviewMedias(bot: $InputUser, lang_code: 'string', order: [$InputMedia, $InputMedia], );
```

