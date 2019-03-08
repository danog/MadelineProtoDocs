---
title: channelMessagesFilter
description: Channel messages filter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelMessagesFilter  
[Back to constructors index](index.md)



Channel messages filter

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exclude\_new\_messages|[Bool](../types/Bool.md) | Optional|Exclude new messages?|
|ranges|Array of [MessageRange](../types/MessageRange.md) | Yes|Ranges|



### Type: [ChannelMessagesFilter](../types/ChannelMessagesFilter.md)


### Example:

```php
$channelMessagesFilter = ['_' => 'channelMessagesFilter', 'exclude_new_messages' => Bool, 'ranges' => [MessageRange, MessageRange]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelMessagesFilter", "exclude_new_messages": Bool, "ranges": [MessageRange]}
```


Or, if you're into Lua:

```lua
channelMessagesFilter={_='channelMessagesFilter', exclude_new_messages=Bool, ranges={MessageRange}}

```


