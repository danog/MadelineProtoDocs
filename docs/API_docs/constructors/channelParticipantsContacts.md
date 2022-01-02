---
title: "channelParticipantsContacts"
description: "Fetch only participants that are also contacts"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsContacts  
[Back to constructors index](index.md)



Fetch only participants that are also contacts

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](../types/string.md) | Yes|Optional search query for searching contact participants by name|



### Type: [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsContacts = ['_' => 'channelParticipantsContacts', 'q' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantsContacts={_='channelParticipantsContacts', q='string'}

```


