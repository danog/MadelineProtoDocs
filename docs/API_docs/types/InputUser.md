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

You can also provide one of the following objects, instead, MadelineProto will handle conversion automatically:  

- [Chat](Chat.html)
- [User](User.html)
- [InputPeer](InputPeer.html)
- [InputDialogPeer](InputDialogPeer.html)
- [InputNotifyPeer](InputNotifyPeer.html)
- [InputUser](InputUser.html)
- [InputChannel](InputChannel.html)
- [Peer](Peer.html)
- [DialogPeer](DialogPeer.html)
- [NotifyPeer](NotifyPeer.html)
- [Chat](Chat.html)




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

