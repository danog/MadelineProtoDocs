---
title: "Getting all chats (dialogs)"
description: "There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting all chats (dialogs)

There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.

* [Dialog list](#getDialogs-now-fully-async)
* [Full dialog info](#getFullDialogs-now-fully-async)

## getDialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->getDialogs();
foreach ($dialogs as $peer) {
    yield $MadelineProto->messages->sendMessage(['peer' => $peer, 'message' => 'Hi! Testing MadelineProto broadcasting!']);
}
```

`getDialogs` will return a full list of all chats you're member of, see [here for the parameters and the result](https://docs.madelineproto.xyz/getDialogs.html)

## getFullDialogs ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html))
```php
$dialogs = yield $MadelineProto->getFullDialogs();
foreach ($dialogs as $dialog) {
    $MadelineProto->logger($dialog);
}
```

`getFullDialogs` will return a full list of all chats you're member of, including dialog info (such as the pinned/last message ID, unread count, tag count, notification settings and message drafts) see [here for the parameters and the result](https://docs.madelineproto.xyz/getFullDialogs.html)

<a href="https://docs.madelineproto.xyz/docs/INLINE_BUTTONS.html">Next section</a>