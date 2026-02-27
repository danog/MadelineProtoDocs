---
title: "danog\\DialogId\\DialogId: Represents the type of a bot API dialog ID."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\DialogId\DialogId`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents the type of a bot API dialog ID.  




## Constants
* `danog\DialogId\DialogId::USER`: Dialog type: user.

* `danog\DialogId\DialogId::CHAT`: Dialog type: chat.

* `danog\DialogId\DialogId::CHANNEL_OR_SUPERGROUP`: Dialog type: supergroup or channel, see https://core.telegram.org/api/channel for more info.

* `danog\DialogId\DialogId::SECRET_CHAT`: Dialog type: secret chat.

* `danog\DialogId\DialogId::MONOFORUM`: Dialog type: monoforum.

## Properties
* `$name`: `string` 

## Method list:
* [`getType(integer $id): \danog\DialogId\DialogId`](#getType)
* [`isSupergroupOrChannel(int $id): bool`](#isSupergroupOrChannel)
* [`isSupergroupOrChannelOrMonoforum(int $id): bool`](#isSupergroupOrChannelOrMonoforum)
* [`isMonoforum(int $id): bool`](#isMonoforum)
* [`isChat(int $id): bool`](#isChat)
* [`isUser(int $id): bool`](#isUser)
* [`isSecretChat(int $id): bool`](#isSecretChat)
* [`fromSecretChatId(int $id): int`](#fromSecretChatId)
* [`toSecretChatId(int $id): int`](#toSecretChatId)
* [`fromSupergroupOrChannelId(int $id): int`](#fromSupergroupOrChannelId)
* [`toSupergroupOrChannelId(int $id): int`](#toSupergroupOrChannelId)
* [`fromChatId(int $id): int`](#fromChatId)
* [`toChatId(int $id): int`](#toChatId)
* [`fromMonoforumId(int $id): int`](#fromMonoforumId)
* [`toMonoforumId(int $id): int`](#toMonoforumId)
* [`fromUserId(int $id): int`](#fromUserId)
* [`toUserId(int $id): int`](#toUserId)
* [`toMTProtoId(int $id): int`](#toMTProtoId)
* [`cases(): array`](#cases)

## Methods:
### <a name="getType"></a> `getType(integer $id): \danog\DialogId\DialogId`

Get the type of a dialog using just its bot API dialog ID.


Parameters:

* `$id`: `integer` Bot API ID.  



### <a name="isSupergroupOrChannel"></a> `isSupergroupOrChannel(int $id): bool`

Checks whether the provided bot API ID is a supergroup or channel ID.


Parameters:

* `$id`: `int`   



### <a name="isSupergroupOrChannelOrMonoforum"></a> `isSupergroupOrChannelOrMonoforum(int $id): bool`

Checks whether the provided bot API ID is a supergroup, channel or monoforum.


Parameters:

* `$id`: `int`   



### <a name="isMonoforum"></a> `isMonoforum(int $id): bool`

Checks whether the provided bot API ID is a monoforum.


Parameters:

* `$id`: `int`   



### <a name="isChat"></a> `isChat(int $id): bool`

Checks whether the provided bot API ID is a chat ID.


Parameters:

* `$id`: `int`   



### <a name="isUser"></a> `isUser(int $id): bool`

Checks whether the provided bot API ID is a user ID.


Parameters:

* `$id`: `int`   



### <a name="isSecretChat"></a> `isSecretChat(int $id): bool`

Checks whether the provided bot API ID is a secret chat ID.


Parameters:

* `$id`: `int`   



### <a name="fromSecretChatId"></a> `fromSecretChatId(int $id): int`

Convert MTProto secret chat ID to bot API secret chat ID.


Parameters:

* `$id`: `int` MTProto secret chat ID  


Return value: Bot API secret chat ID


### <a name="toSecretChatId"></a> `toSecretChatId(int $id): int`

Convert bot API secret chat ID to MTProto secret chat ID.


Parameters:

* `$id`: `int` Bot API secret chat ID  


Return value: MTProto secret chat ID


### <a name="fromSupergroupOrChannelId"></a> `fromSupergroupOrChannelId(int $id): int`

Convert MTProto channel ID to bot API channel ID.


Parameters:

* `$id`: `int` MTProto channel ID  



### <a name="toSupergroupOrChannelId"></a> `toSupergroupOrChannelId(int $id): int`

Convert bot API channel ID to MTProto channel ID.


Parameters:

* `$id`: `int` Bot API channel ID  



### <a name="fromChatId"></a> `fromChatId(int $id): int`

Convert MTProto chat ID to bot API chat ID.


Parameters:

* `$id`: `int` MTProto chat ID  



### <a name="toChatId"></a> `toChatId(int $id): int`

Convert bot API chat ID to MTProto chat ID.


Parameters:

* `$id`: `int` Bot API chat ID  



### <a name="fromMonoforumId"></a> `fromMonoforumId(int $id): int`

Convert MTProto monoforum ID to bot API monoforum ID.


Parameters:

* `$id`: `int` MTProto monoforum ID  



### <a name="toMonoforumId"></a> `toMonoforumId(int $id): int`

Convert bot API monoforum ID to MTProto monoforum ID.


Parameters:

* `$id`: `int` Bot API monoforum ID  



### <a name="fromUserId"></a> `fromUserId(int $id): int`

Convert MTProto user ID to bot API user ID.


Parameters:

* `$id`: `int` MTProto user ID  



### <a name="toUserId"></a> `toUserId(int $id): int`

Convert bot API user ID to MTProto user ID.


Parameters:

* `$id`: `int` Bot API user ID  



### <a name="toMTProtoId"></a> `toMTProtoId(int $id): int`

Convert bot API ID to MTProto ID (automatically detecting the correct type).


Parameters:

* `$id`: `int` Bot API dialog ID  



### <a name="cases"></a> `cases(): array`





---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
