---
title: "bots.checkDownloadFileParams"
description: "Check if a [mini app](https://core.telegram.org/api/bots/webapps) can request the download of a specific file: called when handling [web\_app\_request\_file\_download events »](https://core.telegram.org/api/web-events#web-app-request-file-download)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_checkDownloadFileParams.html
---
# Method: bots.checkDownloadFileParams
[Back to methods index](index.html)



Check if a [mini app](https://core.telegram.org/api/bots/webapps) can request the download of a specific file: called when handling [web\_app\_request\_file\_download events »](https://core.telegram.org/api/web-events#web-app-request-file-download)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot that owns the [mini app](https://core.telegram.org/api/bots/webapps) that requested the download | Optional|
|file\_name|[string](/API_docs/types/string.html) | The `filename` from the [web\_app\_request\_file\_download event »](https://core.telegram.org/api/web-events#web-app-request-file-download) | Optional|
|url|[string](/API_docs/types/string.html) | The `url` from the [web\_app\_request\_file\_download event »](https://core.telegram.org/api/web-events#web-app-request-file-download) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->bots->checkDownloadFileParams(bot: $InputUser, file_name: 'string', url: 'string', );
```

