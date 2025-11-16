---
title: "groupCallMessage"
description: "groupCallMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_admin|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|
|paid\_message\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [GroupCallMessage](/API_docs/types/GroupCallMessage.html)


### Example:

```
$groupCallMessage = ['_' => 'groupCallMessage', 'from_admin' => Bool, 'id' => int, 'from_id' => Peer, 'date' => int, 'message' => TextWithEntities, 'paid_message_stars' => long];
```  
