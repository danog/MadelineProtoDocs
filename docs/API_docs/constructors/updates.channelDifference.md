---
title: "updates.channelDifference"
description: "The new updates"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_channelDifference.html
---
# Constructor: updates.channelDifference  
[Back to constructors index](/API_docs/constructors/index.html)



The new updates

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](/API_docs/types/Bool.html) | Optional|Whether there are more updates to be fetched using getDifference, starting from the provided `pts`|
|pts|[int](/API_docs/types/int.html) | Yes|The [PTS](https://core.telegram.org/api/updates) from which to start getting updates the next time|
|timeout|[int](/API_docs/types/int.html) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed|
|new\_messages|Array of [Message](/API_docs/types/Message.html) | Yes|New messages|
|other\_updates|Array of [Update](/API_docs/types/Update.html) | Yes|Other updates|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)


### Example:

```
$updates_channelDifference = ['_' => 'updates.channelDifference', 'final' => Bool, 'pts' => int, 'timeout' => int, 'new_messages' => [Message, Message], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
