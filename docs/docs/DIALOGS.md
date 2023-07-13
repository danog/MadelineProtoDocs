---
title: "Getting all chats (dialogs)"
description: "There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot."
nav_order: 23
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Getting all chats (dialogs)

There are two ways to get a list of all chats, depending if you logged in as a user, or as a bot.

* [Dialog ID list](#getDialogIds)
* [Dialog list](#getDialogs)
* [Full dialog info](#getFullDialogs)

## getDialogIds
```php
$dialogs = $MadelineProto->getDialogIds();
foreach ($dialogs as $peer) {
    $MadelineProto->messages->sendMessage(peer: $peer, message: 'Hi! Testing MadelineProto broadcasting!');
}
```

`getDialogIds` will return a full list of the bot API IDs of all users/chats/channels known by the bot, see [here for the parameters and the result](https://docs.madelineproto.xyz/getDialogIds.html).  

**Note**: this method will take a **very long time** to return the first time when used with bots: to avoid incurring in timeouts, run the method via CLI (**not web**) OR use the [async background broadcast API](https://docs.madelineproto.xyz/docs/BROADCAST.html), instead.  
After the first broadcast with the broadcast API (i.e. `$id = $MadelineProto->broadcastMessages(...)`) is completed in the background (i.e. `$MadelineProto->getBroadcastProgress($id) === null`), the result of `getDialogIds` will be cached and will be returned immediately.  

## getDialogs
```php
$dialogs = $MadelineProto->getDialogs();
foreach ($dialogs as $peer) {
    $MadelineProto->messages->sendMessage(peer: $peer, message: 'Hi! Testing MadelineProto broadcasting!');
}
```

`getDialogs` will return a full list of all chats you're member of, see [here for the parameters and the result](https://docs.madelineproto.xyz/getDialogs.html)

**Note**: this method will take a **very long time** to return the first time when used with bots: to avoid incurring in timeouts, run the method via CLI (**not web**) OR use the [async background broadcast API](https://docs.madelineproto.xyz/docs/BROADCAST.html), instead.  
After the first broadcast with the broadcast API (i.e. `$id = $MadelineProto->broadcastMessages(...)`) is completed in the background (i.e. `$MadelineProto->getBroadcastProgress($id) === null`), the result of `getDialogs` will be cached and will be returned immediately.  

## getFullDialogs
```php
$dialogs = $MadelineProto->getFullDialogs();
foreach ($dialogs as $dialog) {
    $MadelineProto->logger($dialog);
}
```

`getFullDialogs` will return a full list of all chats you're member of, including dialog info (such as the pinned/last message ID, unread count, tag count, notification settings and message drafts) see [here for the parameters and the result](https://docs.madelineproto.xyz/getFullDialogs.html)

<a href="https://docs.madelineproto.xyz/docs/INLINE_BUTTONS.html">Next section</a>