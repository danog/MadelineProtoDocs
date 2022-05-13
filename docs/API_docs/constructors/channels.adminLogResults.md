---
title: "channels.adminLogResults"
description: "Admin log events"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_adminLogResults.html
---
# Constructor: channels.adminLogResults  
[Back to constructors index](/API_docs/constructors/index.html)



Admin log events

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|events|Array of [ChannelAdminLogEvent](/API_docs/types/ChannelAdminLogEvent.html) | Yes|Admin log events|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in events|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in events|



### Type: [channels.AdminLogResults](/API_docs/types/channels.AdminLogResults.html)


### Example:

```
$channels_adminLogResults = ['_' => 'channels.adminLogResults', 'events' => [ChannelAdminLogEvent, ChannelAdminLogEvent], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
