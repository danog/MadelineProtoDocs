---
title: updates.channelDifferenceEmpty
description: Empty channel difference
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.channelDifferenceEmpty  
[Back to constructors index](index.md)



Empty channel difference

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](../types/Bool.md) | Optional|Final?|
|channel\_pts|[int](../types/int.md) | Yes|Channel pts|
|timeout|[int](../types/int.md) | Optional|Timeout|



### Type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)


### Example:

```php
$updates_channelDifferenceEmpty = ['_' => 'updates.channelDifferenceEmpty', 'final' => Bool, 'channel_pts' => int, 'timeout' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updates.channelDifferenceEmpty", "final": Bool, "channel_pts": int, "timeout": int}
```


Or, if you're into Lua:

```lua
updates_channelDifferenceEmpty={_='updates.channelDifferenceEmpty', final=Bool, channel_pts=int, timeout=int}

```


