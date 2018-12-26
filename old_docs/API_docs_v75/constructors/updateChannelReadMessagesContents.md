---
title: updateChannelReadMessagesContents
description: Update channel read messages contents
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelReadMessagesContents  
[Back to constructors index](index.md)



Update channel read messages contents

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|messages|Array of [int](../types/int.md) | Yes|Messages|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelReadMessagesContents = ['_' => 'updateChannelReadMessagesContents', 'channel_id' => int, 'messages' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChannelReadMessagesContents", "channel_id": int, "messages": [int]}
```


Or, if you're into Lua:

```lua
updateChannelReadMessagesContents={_='updateChannelReadMessagesContents', channel_id=int, messages={int}}

```


