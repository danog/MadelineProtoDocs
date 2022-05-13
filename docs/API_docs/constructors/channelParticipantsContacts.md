---
title: "channelParticipantsContacts"
description: "Fetch only participants that are also contacts"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsContacts  
[Back to constructors index](/API_docs/constructors/index.html)



Fetch only participants that are also contacts

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](/API_docs/types/string.html) | Yes|Optional search query for searching contact participants by name|



### Type: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.html)


### Example:

```
$channelParticipantsContacts = ['_' => 'channelParticipantsContacts', 'q' => 'string'];
```  
