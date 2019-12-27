---
title: messages.getWebPage
description: Get [instant view](https://instantview.telegram.org) page
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getWebPage  
[Back to methods index](index.md)


Get [instant view](https://instantview.telegram.org) page

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|url|[string](../types/string.md) | URL of IV page to fetch | Yes|
|hash|Array of [int](../types/int.md) |  the hash parameter of the previous result of this method | Optional|


### Return type: [WebPage](../types/WebPage.md)

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

Or, if you're into Lua:

```lua
WebPage = messages.getWebPage({url='string', hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|WC_CONVERT_URL_INVALID|WC convert URL invalid|


