---
title: "forumTopic"
description: "forumTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: forumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|my|[Bool](/API_docs/types/Bool.html) | Optional|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|short|[Bool](/API_docs/types/Bool.html) | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|icon\_color|[int](/API_docs/types/int.html) | Yes|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|
|top\_message|[int](/API_docs/types/int.html) | Yes|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|
|unread\_count|[int](/API_docs/types/int.html) | Yes|
|unread\_mentions\_count|[int](/API_docs/types/int.html) | Yes|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|



### Type: [ForumTopic](/API_docs/types/ForumTopic.html)


### Example:

```
$forumTopic = ['_' => 'forumTopic', 'my' => Bool, 'closed' => Bool, 'pinned' => Bool, 'short' => Bool, 'hidden' => Bool, 'id' => int, 'date' => int, 'title' => 'string', 'icon_color' => int, 'icon_emoji_id' => long, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_mentions_count' => int, 'unread_reactions_count' => int, 'from_id' => Peer, 'notify_settings' => PeerNotifySettings, 'draft' => DraftMessage];
```  
