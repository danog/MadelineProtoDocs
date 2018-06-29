---
title: updateChannelReadMessagesContents
description: updateChannelReadMessagesContents attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelReadMessagesContents  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateChannelReadMessagesContents = ['_' => 'updateChannelReadMessagesContents', 'channel_id' => int, 'messages' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChannelReadMessagesContents", "channel_id": int, "messages": [int]}
```


Or, if you're into Lua:  


```
updateChannelReadMessagesContents={_='updateChannelReadMessagesContents', channel_id=int, messages={int}}

```


