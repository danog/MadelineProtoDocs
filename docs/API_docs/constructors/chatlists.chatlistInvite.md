---
title: "chatlists.chatlistInvite"
description: "Info about a chat folder deep link »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistInvite.html
---
# Constructor: chatlists.chatlistInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title\_noanimate|[Bool](/API_docs/types/Bool.html) | Optional|If set, any animated emojis present in `title` should not be animated and should be instead frozen on the first frame.|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Name of the link|
|emoticon|[string](/API_docs/types/string.html) | Optional|Emoji to use as icon for the folder.|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|Supergroups and channels to join|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Related chat information|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related user information|



### Type: [chatlists.ChatlistInvite](/API_docs/types/chatlists.ChatlistInvite.html)


### Example:

```
$chatlists_chatlistInvite = ['_' => 'chatlists.chatlistInvite', 'title_noanimate' => Bool, 'title' => TextWithEntities, 'emoticon' => 'string', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
