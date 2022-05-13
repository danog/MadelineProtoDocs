---
title: "channelParticipantsBanned"
description: "Fetch only banned participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsBanned  
[Back to constructors index](/API_docs/constructors/index.html)



Fetch only banned participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](/API_docs/types/string.html) | Yes|Optional filter for searching banned participants by name (otherwise empty)|



### Type: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.html)


### Example:

```
$channelParticipantsBanned = ['_' => 'channelParticipantsBanned', 'q' => 'string'];
```  
