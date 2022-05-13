---
title: "groupCallParticipantVideoSourceGroup"
description: "Describes a group of video synchronization source identifiers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideoSourceGroup  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a group of video synchronization source identifiers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|semantics|[string](/API_docs/types/string.html) | Yes|SDP semantics|
|sources|Array of [int](/API_docs/types/int.html) | Yes|Source IDs|



### Type: [GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.html)


### Example:

```
$groupCallParticipantVideoSourceGroup = ['_' => 'groupCallParticipantVideoSourceGroup', 'semantics' => 'string', 'sources' => [int, int]];
```  
