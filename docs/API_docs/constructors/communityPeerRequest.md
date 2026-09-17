---
title: "communityPeerRequest"
description: "communityPeerRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: communityPeerRequest  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|visible|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Yes|
|requested\_by|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|



### Type: [CommunityPeerRequest](/API_docs/types/CommunityPeerRequest.html)


### Example:

```
$communityPeerRequest = ['_' => 'communityPeerRequest', 'visible' => Bool, 'peer' => long, 'requested_by' => long, 'date' => int];
```  
