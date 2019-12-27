---
title: channelParticipantsSearch
description: Query participants by name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsSearch  
[Back to constructors index](index.md)



Query participants by name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](../types/string.md) | Yes|Search query|



### Type: [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsSearch = ['_' => 'channelParticipantsSearch', 'q' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantsSearch={_='channelParticipantsSearch', q='string'}

```


