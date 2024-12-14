---
title: "premium.getMyBoosts"
description: "Obtain which peers are we currently [boosting](https://core.telegram.org/api/boost), and how many [boost slots](https://core.telegram.org/api/boost) we have left."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/premium_getMyBoosts.html
---
# Method: premium.getMyBoosts
[Back to methods index](index.html)



Obtain which peers are we currently [boosting](https://core.telegram.org/api/boost), and how many [boost slots](https://core.telegram.org/api/boost) we have left.



### Return type: [premium.MyBoosts](/API_docs/types/premium.MyBoosts.html)

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

$premium_MyBoosts = $MadelineProto->premium->getMyBoosts();
```

