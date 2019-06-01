---
title: Getting all chats (dialogs)
description: There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting all chats (dialogs)

There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.

* [As user](#user-get_dialogs)
    * [Full dialog info](#user-get_full_dialogs)
* [As bot](#bot-internal-peer-database)

## User: get_dialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
    yield $MadelineProto->messages->sendMessage(['peer' => $peer, 'message' => 'Hi! Testing MadelineProto broadcasting!']);
}
```

`get_dialogs` will return a full list of all chats you're member of, see [here for the parameters and the result](https://docs.madelineproto.xyz/get_dialogs.html)

## User: get_full_dialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->get_full_dialogs();
foreach ($dialogs as $dialog) {
    \danog\MadelineProto\Logger::log($dialog);
}
```

`get_full_dialogs` will return a full list of all chats you're member of, including dialog info (such as the pinned/last message ID, unread count, tag count, notification settings and message drafts) see [here for the parameters and the result](https://docs.madelineproto.xyz/get_full_dialogs.html)

## Bot: internal peer database
```php
foreach ($MadelineProto->API->chats as $bot_api_id => $chat) {
    try {
        yield $MadelineProto->messages->sendMessage(['peer' => $chat, 'message' => "Hi $bot_api_id! Testing MadelineProto broadcasting!"]);
    } catch (\danog\MadelineProto\RPCErrorException $e) {
        echo $e;
    }
}
```

Since bots cannot run `get_dialogs`, you must make use of the internal MadelineProto database to get a list of all users, chats and channels MadelineProto has seen.
`$MadelineProto->API->chats` contains a list of [Chat](../API_docs/types/Chat.html) and [User](../API_docs/types/User.html) objects, indexed by bot API id.

<a href="https://docs.madelineproto.xyz/docs/INLINE_BUTTONS.html">Next section</a>