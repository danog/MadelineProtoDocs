---
title: "stories.togglePinnedToTop"
description: "Pin some stories to the top of the profile, see [here »](https://core.telegram.org/api/stories#pinned-or-archived-stories) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_togglePinnedToTop.html
---
# Method: stories.togglePinnedToTop
[Back to methods index](index.html)



Pin some stories to the top of the profile, see [here »](https://core.telegram.org/api/stories#pinned-or-archived-stories) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where to pin stories. | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of the stories to pin (max [stories\_pinned\_to\_top\_count\_max](https://core.telegram.org/api/config#stories-pinned-to-top-count-max)). | Yes|


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

$Bool = $MadelineProto->stories->togglePinnedToTop(peer: $InputPeer, id: [$int, $int], );
```

