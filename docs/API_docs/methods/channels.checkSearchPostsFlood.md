---
title: "channels.checkSearchPostsFlood"
description: "channels.checkSearchPostsFlood parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_checkSearchPostsFlood.html
---
# Method: channels.checkSearchPostsFlood
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query|[string](/API_docs/types/string.html) | Optional|


### Return type: [SearchPostsFlood](/API_docs/types/SearchPostsFlood.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$SearchPostsFlood = $MadelineProto->channels->checkSearchPostsFlood(query: 'string', );
```

