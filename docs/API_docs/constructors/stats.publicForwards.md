---
title: "stats.publicForwards"
description: "Contains info about the forwards of a story as a message to public chats and reposts by public channels."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_publicForwards.html
---
# Constructor: stats.publicForwards  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about the forwards of a [story](https://core.telegram.org/api/stories) as a message to public chats and reposts by public channels.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results|
|forwards|Array of [PublicForward](/API_docs/types/PublicForward.html) | Yes|Info about the forwards of a story.|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset used for [pagination](https://core.telegram.org/api/offsets).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stats.PublicForwards](/API_docs/types/stats.PublicForwards.html)


### Example:

```
$stats_publicForwards = ['_' => 'stats.publicForwards', 'count' => int, 'forwards' => [PublicForward, PublicForward], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
