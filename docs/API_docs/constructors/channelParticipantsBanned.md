---
title: "channelParticipantsBanned"
description: "Fetch only banned participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsBanned  
[Back to constructors index](/API_docs/constructors/index.md)



Fetch only banned participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](/API_docs/types/string.md) | Yes|Optional filter for searching banned participants by name (otherwise empty)|



### Type: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsBanned = ['_' => 'channelParticipantsBanned', 'q' => 'string'];
```  
