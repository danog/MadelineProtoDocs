---
title: "exportedChatlistInvite"
description: "Exported chat folder deep link »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: exportedChatlistInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Exported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Name of the link|
|url|[string](/API_docs/types/string.html) | Yes|The [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|Peers to import|



### Type: [ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html)


### Example:

```
$exportedChatlistInvite = ['_' => 'exportedChatlistInvite', 'title' => 'string', 'url' => 'string', 'peers' => [Peer, Peer]];
```  
