---
title: channelMessagesFilter
description: Filter for getting only certain types of channel messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelMessagesFilter  
[Back to constructors index](index.md)



Filter for getting only certain types of channel messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ranges|Array of [MessageRange](../types/MessageRange.md) | Yes|Ranges|



### Type: [ChannelMessagesFilter](../types/ChannelMessagesFilter.md)


### Example:

```php
$channelMessagesFilter = ['_' => 'channelMessagesFilter', 'ranges' => [MessageRange, MessageRange]];
```  


Or, if you're into Lua:

```lua
channelMessagesFilter={_='channelMessagesFilter', ranges={MessageRange}}

```


