---
title: "stats.publicForwards"
description: "stats.publicForwards attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_publicForwards.html
---
# Constructor: stats.publicForwards  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|forwards|Array of [PublicForward](/API_docs/types/PublicForward.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stats.PublicForwards](/API_docs/types/stats.PublicForwards.html)


### Example:

```
$stats_publicForwards = ['_' => 'stats.publicForwards', 'count' => int, 'forwards' => [PublicForward, PublicForward], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
