---
title: "Getting info about chats"
description: "There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects."
nav_order: 18
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting info about chats

There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects.

* [Full chat info with full list of participants](#getPwrChat-now-fully-async)
* [Full chat info](#getFullInfo-now-fully-async)
* [Reduced chat info (very fast)](#getInfo-now-fully-async)
* [Just the chat ID (extremely fast)](#getId-now-fully-async)

## getPwrChat ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$pwr_chat = yield $MadelineProto->getPwrChat(-100214891824);
foreach ($pwr_chat['participants'] as $participant) {
    \danog\MadelineProto\Logger::log($participant);
}
```

Use `getPwrChat` to get full chat info, including the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/getPwrChat.html).  

* Completeness: full
* Speed: medium
* Caching: medium

## getFullInfo ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$full_chat = yield $MadelineProto->getFullInfo(-10028941842);
```

You can also use `getFullInfo` to get full chat info, without the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/getFullInfo.html).  

* Completeness: medium
* Speed: medium-fast
* Caching: full

## getInfo ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$chat = yield $MadelineProto->getInfo(-10028941842);
```

You can also use `getInfo` to get chat info, see [here for the parameters and the result](https://docs.madelineproto.xyz/getInfo.html)

* Completeness: small
* Speed: very fast
* Caching: full

## getId ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$id = yield $MadelineProto->getID($update);
```

You can also use `getId` to get chat ID from updates, messages and other objects.

* Speed: very fast
* Caching: full

<a href="https://docs.madelineproto.xyz/docs/DIALOGS.html">Next section</a>