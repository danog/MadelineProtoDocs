---
title: "Using methods"
description: "There are simplifications for many, if not all of, these methods."
nav_order: 24
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Using methods

There are simplifications for many, if not all of, these methods.

A list of all of the methods that can be called with MadelineProto can be found here: [here (layer 143)](https://docs.madelineproto.xyz/API_docs/).

 [Now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)

* [Named arguments (PHP 8+)](#named-arguments)
* [Peers](#peers)
* [Files](https://docs.madelineproto.xyz/docs/FILES.html)
* [Secret chats](#secret-chats)
* [Entities (Markdown & HTML)](#entities)
* [reply_markup (keyboards & inline keyboards)](#reply_markup)
* [bot API objects](#bot-api-objects)
* [No result](#no-result)
* [Queues](#queues)
* [Multiple method calls](#multiple-method-calls)
* [FULL API Documentation with descriptions](https://docs.madelineproto.xyz/API_docs/methods/)

## Named arguments

MadelineProto supports PHP 7, but PHP 8.1+ is recommended.

On PHP 8, you can use named arguments instead of arrays to provide method arguments, which allows for much cleaner syntax:

```php
yield $MadelineProto->messages->sendMessage(peer: '@danogentili', message: 'Testing MadelineProto...');
```

On PHP 7, you can use the old array syntax, instead:

```php
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'Testing MadelineProto...']);
```


## Peers
[Full example](https://github.com/danog/MadelineProto/blob/master/bot.php)

If an object of type User, InputUser, Chat, InputChannel, Peer or InputPeer must be provided as a parameter to a method, you can substitute it with the user/group/channel's username (`@username`), bot API id (`-1029449`, `1249421`, `-100412412901`), or update.  

```php
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'Testing MadelineProto...']);
```

If you want to check if a bot API id is a supergroup/channel ID:
```php
$Bool = yield $MadelineProto->isSupergroup($id);
```

Uses logarithmic conversion to avoid problems on 32 bit systems.


If you want to convert an MTProto API id to a supergroup/channel bot API ID:
```php
$bot_api_id = yield $MadelineProto->toSupergroup($id);
```

Uses logarithmic conversion to avoid problems on 32 bit systems.


## Secret chats
[Full example](https://github.com/danog/MadelineProto/blob/master/secret_bot.php)
If an object of type InputSecretChat must be provided as a parameter to a method, you can substitute it with the secret chat's id, the updateNewEncrypted message or the decryptedMessage:

```php
yield $MadelineProto->messages->sendEncrypted(['peer' => $update, 'message' => ['_' => 'decryptedMessage', 'ttl' => 0, 'message' => 'Hi']]);
```


## Entities
[Full example](https://github.com/danog/MadelineProto/blob/master/tests/testing.php)
Methods that allow sending message entities ([messages.sendMessage](http://docs.madelineproto.xyz/API_docs/methods/messages_sendMessage.html) for example) also have an additional `parse_mode` parameter that enables or disables html/markdown parsing of the message to be sent.

```php
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => '[Testing Markdown in MadelineProto](https://docs.madelineproto.xyz)', 'parse_mode' => 'Markdown']);
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => '<a href="https://docs.madelineproto.xyz">Testing HTML in MadelineProto</a>', 'parse_mode' => 'HTML']);
```



## reply_markup
reply_markup accepts bot API reply markup objects as well as MTProto ones.

```php
$bot_API_markup = ['inline_keyboard' => 
    [
        [
            ['text' => 'MadelineProto docs', 'url' => 'https://docs.madelineproto.xyz'],
            ['text' => 'MadelineProto channel', 'url' => 'https://t.me/MadelineProto']
        ]
    ]
];
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'lel', 'reply_markup' => $bot_API_markup]);
```


## Bot API objects
To convert the results of methods to bot API objects you must provide a second parameter to method wrappers, containing an array with the `botAPI` key set to true.

```php
$bot_API_object = yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'lel'], ['botAPI' => true]);
```

MadelineProto also [supports bot API file IDs when working with files](FILES.html)


## No result

Also see [ignored async](https://docs.madelineproto.xyz/docs/ASYNC.html#ignored-async).  
To disable fetching the result of a method, the array that must be provided as second parameter to method wrapper must have the `noResponse` key set to true.

```php
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'lel'], ['noResponse' => true]);
```


## Queues
Method calls may be executed at diferent times server-side: to avoid this, method calls can be queued (this is especially useful when using [ignored async](https://docs.madelineproto.xyz/docs/ASYNC.html#ignored-async)):

```php
yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'lel'], ['queue' => 'queue_name']);
```

If the queue if the specified queue name does not exist, it will be created.

## Multiple method calls
See [multiple async](https://docs.madelineproto.xyz/docs/ASYNC.html#multiple-async).  

<a href="https://docs.madelineproto.xyz/docs/CONTRIB.html">Next section</a>