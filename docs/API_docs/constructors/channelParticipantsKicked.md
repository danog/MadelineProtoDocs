---
title: "channelParticipantsKicked"
description: "Fetch only kicked participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsKicked  
[Back to constructors index](/API_docs/constructors/index.md)



Fetch only kicked participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](/API_docs/types/string.md) | Yes|Optional filter for searching kicked participants by name (otherwise empty)|



### Type: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsKicked = ['_' => 'channelParticipantsKicked', 'q' => 'string'];
```  
