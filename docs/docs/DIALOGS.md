---
title: Getting all chats (dialogs)
description: There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting all chats (dialogs)

There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.

* [Dialog list](#get_dialogs-now-fully-async)
* [Full dialog info](#get_full_dialogs-now-fully-async)

## get_dialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->get_dialogs();
foreach ($dialogs as $peer) {
    yield $MadelineProto->messages->sendMessage(['peer' => $peer, 'message' => 'Hi! Testing MadelineProto broadcasting!']);
}
```

`get_dialogs` will return a full list of all chats you're member of, see [here for the parameters and the result](https://docs.madelineproto.xyz/get_dialogs.html)

## get_full_dialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->get_full_dialogs();
foreach ($dialogs as $dialog) {
    $MadelineProto->logger($dialog);
}
```

`get_full_dialogs` will return a full list of all chats you're member of, including dialog info (such as the pinned/last message ID, unread count, tag count, notification settings and message drafts) see [here for the parameters and the result](https://docs.madelineproto.xyz/get_full_dialogs.html)

<a href="https://docs.madelineproto.xyz/docs/INLINE_BUTTONS.html">Next section</a>