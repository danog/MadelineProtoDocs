You can directly provide the [Update](Update.html) or [Message](Message.html) object here, MadelineProto will automatically extract the destination chat id.

The following syntaxes can also be used:

```php
$%1$s = '@username'; // Username

$%1$s = $update; // Update objects received in the event handler

$%1$s = 'me'; // The currently logged-in user

$%1$s = 44700; // bot API id (users)
$%1$s = -492772765; // bot API id (chats)
$%1$s = -10038575794; // bot API id (channels)

$%1$s = 'https://t.me/danogentili'; // t.me URLs
$%1$s = 'https://t.me/joinchat/asfln1-21fa_'; // t.me invite links

```

A [Chat](Chat.html), a [User](User.html), an [InputPeer](InputPeer.html), an [InputDialogPeer](InputDialogPeer.html), an [InputNotifyPeer](InputNotifyPeer.html), an [InputUser](InputUser.html), an [InputChannel](InputChannel.html), a [Peer](Peer.html), an [DialogPeer](DialogPeer.html), [NotifyPeer](NotifyPeer.html), or a [Chat](Chat.html) object can also be used.


