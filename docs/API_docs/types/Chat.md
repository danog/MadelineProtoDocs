---
title: Chat
description: constructors and methods of type Chat
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: Chat
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$Chat = '@username'; // Username

$Chat = $update; // Update objects received in the event handler

$Chat = 'me'; // The currently logged-in user

$Chat = 44700; // bot API id (users)
$Chat = -492772765; // bot API id (chats)
$Chat = -10038575794; // bot API id (channels)

$Chat = 'https://t.me/danogentili'; // t.me URLs
$Chat = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.




### Possible values (constructors):

[chatEmpty](/API_docs/constructors/chatEmpty.html)  

[chat](/API_docs/constructors/chat.html)  

[chatForbidden](/API_docs/constructors/chatForbidden.html)  

[channel](/API_docs/constructors/channel.html)  

[channelForbidden](/API_docs/constructors/channelForbidden.html)  



### Methods that return an object of this type (methods):



[chatEmpty](/API_docs/constructors/chatEmpty.html)  

[chat](/API_docs/constructors/chat.html)  

[chatForbidden](/API_docs/constructors/chatForbidden.html)  

[channel](/API_docs/constructors/channel.html)  

[channelForbidden](/API_docs/constructors/channelForbidden.html)  

