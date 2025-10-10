---
title: "forumTopic"
description: "Represents a forum topic."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: forumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [forum topic](https://core.telegram.org/api/forum#forum-topics).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|my|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was created by the current user|
|closed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic is closed (no messages can be sent to it)|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic is pinned|
|short|[Bool](/API_docs/types/Bool.html) | Optional|Whether this constructor is a reduced version of the full topic information. <br>If set, only the `my`, `closed`, `id`, `date`, `title`, `icon_color`, `icon_emoji_id` and `from_id` parameters will contain valid information. <br>Reduced info is usually only returned in topic-related [admin log events »](https://core.telegram.org/api/recent-actions) and in the [messages.channelMessages](../constructors/messages.channelMessages.html) constructor: if needed, full information can be fetched using [channels.getForumTopicsByID](../methods/channels.getForumTopicsByID.html).|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic is hidden (only valid for the "General" topic, `id=1`)|
|title\_missing|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|[Topic ID](https://core.telegram.org/api/forum#forum-topics)|
|date|[int](/API_docs/types/int.html) | Yes|Topic creation date|
|peer|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|Topic title|
|icon\_color|[int](/API_docs/types/int.html) | Yes|If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of `0x6FB9F0`, `0xFFD67E`, `0xCB86DB`, `0x8EEE98`, `0xFF93B2`, or `0xFB6F5F`.|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|ID of the [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon.|
|top\_message|[int](/API_docs/types/int.html) | Yes|ID of the last message that was sent to this topic|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages|
|unread\_mentions\_count|[int](/API_docs/types/int.html) | Yes|Number of [unread mentions](https://core.telegram.org/api/mentions)|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|Number of unread reactions to messages you sent|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|ID of the peer that created the topic|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|Notification settings|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|Message [draft](https://core.telegram.org/api/drafts)|



### Type: [ForumTopic](/API_docs/types/ForumTopic.html)


### Example:

```
$forumTopic = ['_' => 'forumTopic', 'my' => Bool, 'closed' => Bool, 'pinned' => Bool, 'short' => Bool, 'hidden' => Bool, 'title_missing' => Bool, 'id' => int, 'date' => int, 'peer' => long, 'title' => 'string', 'icon_color' => int, 'icon_emoji_id' => long, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_mentions_count' => int, 'unread_reactions_count' => int, 'from_id' => Peer, 'notify_settings' => PeerNotifySettings, 'draft' => DraftMessage];
```  
