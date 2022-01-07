---
title: InputUser
description: constructors and methods of type InputUser
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: InputUser
[Back to types index](index.html)

You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$InputUser = '@username'; // Username

$InputUser = $update; // Update objects received in the event handler

$InputUser = 'me'; // The currently logged-in user

$InputUser = 44700; // bot API id (users)
$InputUser = -492772765; // bot API id (chats)
$InputUser = -10038575794; // bot API id (channels)

$InputUser = 'https://t.me/danogentili'; // t.me URLs
$InputUser = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.




### Possible values (constructors):

[inputUserEmpty](/API_docs/constructors/inputUserEmpty.html)  

[inputUserSelf](/API_docs/constructors/inputUserSelf.html)  

[inputUser](/API_docs/constructors/inputUser.html)  

[inputUserFromMessage](/API_docs/constructors/inputUserFromMessage.html)  



### Methods that return an object of this type (methods):



[inputUserEmpty](/API_docs/constructors/inputUserEmpty.html)  

[inputUserSelf](/API_docs/constructors/inputUserSelf.html)  

[inputUser](/API_docs/constructors/inputUser.html)  

[inputUserFromMessage](/API_docs/constructors/inputUserFromMessage.html)  

