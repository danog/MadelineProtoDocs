---
title: "contacts.block"
description: "Adds a peer to a blocklist, see [here »](https://core.telegram.org/api/block) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_block.html
---
# Method: contacts.block
[Back to methods index](index.html)



Adds a peer to a blocklist, see [here »](https://core.telegram.org/api/block) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Whether the peer should be added to the story blocklist; if not set, the peer will be added to the main blocklist, see [here »](https://core.telegram.org/api/block) for more info. | Optional|
|id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|


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

$Bool = $MadelineProto->contacts->block(my_stories_from: $Bool, id: $InputPeer, );
```

