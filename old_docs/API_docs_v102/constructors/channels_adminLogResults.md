---
title: channels.adminLogResults
description: Admin log results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channels.adminLogResults  
[Back to constructors index](index.md)



Admin log results

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|events|Array of [ChannelAdminLogEvent](../types/ChannelAdminLogEvent.md) | Yes|Events|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [channels\_AdminLogResults](../types/channels_AdminLogResults.md)


### Example:

```php
$channels_adminLogResults = ['_' => 'channels.adminLogResults', 'events' => [ChannelAdminLogEvent, ChannelAdminLogEvent], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
channels_adminLogResults={_='channels.adminLogResults', events={ChannelAdminLogEvent}, chats={Chat}, users={User}}

```


