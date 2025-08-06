---
title: "messages.getWebPage"
description: "Get [instant view](https://instantview.telegram.org) page"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getWebPage.html
---
# Method: messages.getWebPage
[Back to methods index](index.html)



Get [instant view](https://instantview.telegram.org) page

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|url|[string](/API_docs/types/string.html) | URL of IV page to fetch | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [messages.WebPage](/API_docs/types/messages.WebPage.html)

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

$messages_WebPage = $MadelineProto->messages->getWebPage(url: 'string', hash: [$long\|string, $long\|string], );
```

