---
title: "contacts.setBlocked"
description: "Replace the contents of an entire [blocklist, see here for more info »](https://core.telegram.org/api/block)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_setBlocked.html
---
# Method: contacts.setBlocked
[Back to methods index](index.html)



Replace the contents of an entire [blocklist, see here for more info »](https://core.telegram.org/api/block).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Whether to edit the story blocklist; if not set, will edit the main blocklist. See [here »](https://core.telegram.org/api/block) for differences between the two. | Optional|
|id|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Full content of the blocklist. | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->contacts->setBlocked(my_stories_from: $Bool, id: [$InputPeer, $InputPeer], limit: $int, );
```

