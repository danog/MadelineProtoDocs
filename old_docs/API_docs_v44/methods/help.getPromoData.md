---
title: help.getPromoData
description: Get MTProxy/Public Service Announcement information
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPromoData.html
---
# Method: help.getPromoData
[Back to methods index](index.md)



Get MTProxy/Public Service Announcement information



### Return type: [help.PromoData](../types/help.PromoData.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_PromoData = $MadelineProto->help->getPromoData();
```

Or, if you're into Lua:

```lua
help_PromoData = help.getPromoData({})
```

