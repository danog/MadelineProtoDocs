---
title: "Getting info about chats"
description: "There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects."
nav_order: 22
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting info about chats

There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects.

* [Full chat info with full list of participants](#getPwrChat)
* [Full chat info](#getFullInfo)
* [Reduced chat info (very fast)](#getInfo)
* [Just the chat ID (extremely fast)](#getId)

## getPwrChat
```php
$pwr_chat = $MadelineProto->getPwrChat(-100214891824);
foreach ($pwr_chat['participants'] as $participant) {
    \danog\MadelineProto\Logger::log($participant);
}
```

Use `getPwrChat` to get full chat info, including the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/getPwrChat.html).  

Please avoid using this method if possible, use [getInfo](#getinfo) or at least [getFullInfo](#getfullinfo) to avoid flood waits.

* Speed: slow
* Caching: partial

## getFullInfo
```php
$full_chat = $MadelineProto->getFullInfo(-10028941842);
```

You can use `getFullInfo` to get full chat info, without the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/getFullInfo.html).

Please avoid using this method if possible, use [getInfo](#getinfo) to avoid flood waits.  

* Speed: medium-fast
* Caching: partial, and an initial RPC query is always made, so please use [getInfo](#getinfo) if possible to avoid flood waits.

## getInfo
```php
$chat = $MadelineProto->getInfo(-10028941842);
```

You can use `getInfo` to get chat info, see [here for the parameters and the result](https://docs.madelineproto.xyz/getInfo.html)

* Speed: fast
* Caching: full, 0 RPC queries are made unless an unknown username is passed.

## getId
```php
$id = $MadelineProto->getID($update);
```

You can also use `getId` to get chat ID from updates, messages and other objects.

* Speed: very fast
* Caching: full, 0 RPC queries are made unless an unknown username is passed.

<a href="https://docs.madelineproto.xyz/docs/DIALOGS.html">Next section</a>