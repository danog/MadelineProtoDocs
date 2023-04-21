---
title: "exportedChatlistInvite"
description: "exportedChatlistInvite attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: exportedChatlistInvite  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|url|[string](/API_docs/types/string.html) | Yes|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|



### Type: [ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html)


### Example:

```
$exportedChatlistInvite = ['_' => 'exportedChatlistInvite', 'title' => 'string', 'url' => 'string', 'peers' => [Peer, Peer]];
```  
