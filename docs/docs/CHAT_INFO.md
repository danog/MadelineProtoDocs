---
title: Getting info about chats
description: There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting info about chats

There are various methods that can be used to fetch info about chats, based on bot API id, tg-cli ID, Peer, User, Chat objects.

* [Full chat info with full list of participants](#get_pwr_chat)
* [Full chat info](#get_full_info)
* [Reduced chat info (very fast)](#get_info)

## get_pwr_chat ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$pwr_chat = yield $MadelineProto->get_pwr_chat(-100214891824);
foreach ($pwr_chat['participants'] as $participant) {
    \danog\MadelineProto\Logger::log($participant);
}
```

Use `get_pwr_chat` to get full chat info, including the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/get_pwr_chat.html).  

* Completeness: full
* Speed: medium
* Caching: medium

## get_full_info ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$full_chat = yield $MadelineProto->get_full_info(-10028941842);
```

You can also use `get_full_info` to get full chat info, without the full list of members, see [here for the parameters and the result](https://docs.madelineproto.xyz/get_full_info.html).  

* Completeness: medium
* Speed: medium-fast
* Caching: full

## get_info ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$chat = yield $MadelineProto->get_info(-10028941842);
```

You can also use `get_info` to get chat info, see [here for the parameters and the result](https://docs.madelineproto.xyz/get_info.html)

* Completeness: small
* Speed: very fast
* Caching: full

<a href="https://docs.madelineproto.xyz/docs/DIALOGS.html">Next section</a>