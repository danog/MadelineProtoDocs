---
title: "messages.chatInviteJoinResultWebView"
description: "messages.chatInviteJoinResultWebView attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatInviteJoinResultWebView.html
---
# Constructor: messages.chatInviteJoinResultWebView  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.ChatInviteJoinResult](/API_docs/types/messages.ChatInviteJoinResult.html)


### Example:

```
$messages_chatInviteJoinResultWebView = ['_' => 'messages.chatInviteJoinResultWebView', 'bot_id' => long, 'query_id' => long, 'users' => [User, User]];
```  
