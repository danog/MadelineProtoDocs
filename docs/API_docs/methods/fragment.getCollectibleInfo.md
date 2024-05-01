---
title: "fragment.getCollectibleInfo"
description: "fragment.getCollectibleInfo parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/fragment_getCollectibleInfo.html
---
# Method: fragment.getCollectibleInfo
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collectible|[InputCollectible](/API_docs/types/InputCollectible.html) | Yes|


### Return type: [fragment.CollectibleInfo](/API_docs/types/fragment.CollectibleInfo.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$fragment_CollectibleInfo = $MadelineProto->fragment->getCollectibleInfo(collectible: $InputCollectible, );
```

