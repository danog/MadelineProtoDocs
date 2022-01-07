---
title: "messages.getWebPage"
description: "Get [instant view](https://instantview.telegram.org) page"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getWebPage.html
---
# Method: messages.getWebPage
[Back to methods index](index.md)



Get [instant view](https://instantview.telegram.org) page

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|url|[string](/API_docs/types/string.md) | URL of IV page to fetch | Yes|
|hash|Array of [int](/API_docs/types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [WebPage](/API_docs/types/WebPage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WebPage = $MadelineProto->messages->getWebPage(['url' => 'string', 'hash' => [int, int], ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|WC_CONVERT_URL_INVALID|WC convert URL invalid|


