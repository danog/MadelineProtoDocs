---
title: "contacts.resetTopPeerRating"
description: "Reset [rating](https://core.telegram.org/api/top-rating) of top peer"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_resetTopPeerRating.html
---
# Method: contacts.resetTopPeerRating
[Back to methods index](index.html)



Reset [rating](https://core.telegram.org/api/top-rating) of top peer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|category|[TopPeerCategory](/API_docs/types/TopPeerCategory.html) | Top peer category | Yes|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose rating should be reset | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->contacts->resetTopPeerRating(category: TopPeerCategory, peer: InputPeer, );
```

