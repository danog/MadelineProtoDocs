---
title: "channelParticipantsKicked"
description: "Fetch only kicked participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsKicked  
[Back to constructors index](index.md)



Fetch only kicked participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](../types/string.md) | Yes|Optional filter for searching kicked participants by name (otherwise empty)|



### Type: [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsKicked = ['_' => 'channelParticipantsKicked', 'q' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantsKicked={_='channelParticipantsKicked', q='string'}

```


