---
title: "channelParticipantsBanned"
description: "Fetch only banned participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsBanned  
[Back to constructors index](index.md)



Fetch only banned participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](../types/string.md) | Yes|Optional filter for searching banned participants by name (otherwise empty)|



### Type: [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsBanned = ['_' => 'channelParticipantsBanned', 'q' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantsBanned={_='channelParticipantsBanned', q='string'}

```


