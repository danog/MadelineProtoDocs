---
title: "channels.getGroupsForDiscussion"
description: "Get all groups that can be used as [discussion groups](https://core.telegram.org/api/discussion)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getGroupsForDiscussion.html
---
# Method: channels.getGroupsForDiscussion
[Back to methods index](index.html)



Get all groups that can be used as [discussion groups](https://core.telegram.org/api/discussion).

Returned [basic group chats](https://core.telegram.org/api/channel#basic-groups) must be first upgraded to [supergroups](https://core.telegram.org/api/channel#supergroups) before they can be set as a discussion group.  
To set a returned supergroup as a discussion group, access to its old messages must be enabled using [channels.togglePreHistoryHidden](../methods/channels.togglePreHistoryHidden.html), first.



### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_Chats = $MadelineProto->channels->getGroupsForDiscussion();
```

