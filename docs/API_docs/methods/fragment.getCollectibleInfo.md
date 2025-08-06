---
title: "fragment.getCollectibleInfo"
description: "Fetch information about a [fragment collectible, see here »](https://core.telegram.org/api/fragment#fetching-info-about-fragment-collectibles) for more info on the full flow."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/fragment_getCollectibleInfo.html
---
# Method: fragment.getCollectibleInfo
[Back to methods index](index.html)



Fetch information about a [fragment collectible, see here »](https://core.telegram.org/api/fragment#fetching-info-about-fragment-collectibles) for more info on the full flow.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|collectible|[InputCollectible](/API_docs/types/InputCollectible.html) | Collectible to fetch info about. | Yes|


### Return type: [fragment.CollectibleInfo](/API_docs/types/fragment.CollectibleInfo.html)

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

$fragment_CollectibleInfo = $MadelineProto->fragment->getCollectibleInfo(collectible: $InputCollectible, );
```

