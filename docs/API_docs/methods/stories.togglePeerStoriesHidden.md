---
title: "stories.togglePeerStoriesHidden"
description: "Hide the active stories of a user, preventing them from being displayed on the action bar on the homescreen, see [here »](https://core.telegram.org/api/stories#hiding-stories-of-other-users) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_togglePeerStoriesHidden.html
---
# Method: stories.togglePeerStoriesHidden
[Back to methods index](index.html)



Hide the active stories of a user, preventing them from being displayed on the action bar on the homescreen, see [here »](https://core.telegram.org/api/stories#hiding-stories-of-other-users) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose stories should be (un)hidden. | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | Whether to hide or unhide stories. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->stories->togglePeerStoriesHidden(peer: $InputPeer, hidden: $Bool, );
```

