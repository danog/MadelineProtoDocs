---
title: "contacts.getTopPeers"
description: "Get most used peers"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getTopPeers.html
---
# Method: contacts.getTopPeers
[Back to methods index](index.html)



Get most used peers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|correspondents|[Bool](/API_docs/types/Bool.html) | Users we've chatted most frequently with | Optional|
|bots\_pm|[Bool](/API_docs/types/Bool.html) | Most used bots | Optional|
|bots\_inline|[Bool](/API_docs/types/Bool.html) | Most used inline bots | Optional|
|phone\_calls|[Bool](/API_docs/types/Bool.html) | Most frequently called users | Optional|
|forward\_users|[Bool](/API_docs/types/Bool.html) | Users to which the users often forwards messages to | Optional|
|forward\_chats|[Bool](/API_docs/types/Bool.html) | Chats to which the users often forwards messages to | Optional|
|groups|[Bool](/API_docs/types/Bool.html) | Often-opened groups and supergroups | Optional|
|channels|[Bool](/API_docs/types/Bool.html) | Most frequently visited channels | Optional|
|offset|[int](/API_docs/types/int.html) | Offset for [pagination](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [contacts.TopPeers](/API_docs/types/contacts.TopPeers.html)

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
$contacts_TopPeers = $MadelineProto->contacts->getTopPeers(correspondents: Bool, bots_pm: Bool, bots_inline: Bool, phone_calls: Bool, forward_users: Bool, forward_chats: Bool, groups: Bool, channels: Bool, offset: int, limit: int, hash: long, );
```

