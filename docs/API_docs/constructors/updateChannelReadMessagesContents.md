---
title: "updateChannelReadMessagesContents"
description: "The specified channel/supergroup messages were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelReadMessagesContents  
[Back to constructors index](index.md)



The specified [channel/supergroup](https://core.telegram.org/api/channel) messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|IDs of messages that were read|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelReadMessagesContents = ['_' => 'updateChannelReadMessagesContents', 'channel_id' => long, 'messages' => [int, int]];
```  


Or, if you're into Lua:

```lua
updateChannelReadMessagesContents={_='updateChannelReadMessagesContents', channel_id=long, messages={int}}

```


