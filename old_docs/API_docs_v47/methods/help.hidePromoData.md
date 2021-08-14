---
title: help.hidePromoData
description: Hide MTProxy/Public Service Announcement information
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_hidePromoData.html
---
# Method: help.hidePromoData
[Back to methods index](index.md)



Hide MTProxy/Public Service Announcement information

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer to hide | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->help->hidePromoData(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Bool = help.hidePromoData({peer=InputPeer, })
```

