---
title: channelMessagesFilter
description: channelMessagesFilter attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: channelMessagesFilter  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|important\_only|[Bool](../types/Bool.md) | Optional|
|ranges|Array of [MessageRange](../types/MessageRange.md) | Yes|



### Type: [ChannelMessagesFilter](../types/ChannelMessagesFilter.md)


### Example:

```
$channelMessagesFilter = ['_' => 'channelMessagesFilter', 'important_only' => Bool, 'ranges' => [MessageRange, MessageRange]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelMessagesFilter", "important_only": Bool, "ranges": [MessageRange]}
```


Or, if you're into Lua:  


```
channelMessagesFilter={_='channelMessagesFilter', important_only=Bool, ranges={MessageRange}}

```


