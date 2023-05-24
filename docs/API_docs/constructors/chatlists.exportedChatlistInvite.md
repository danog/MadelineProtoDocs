---
title: "chatlists.exportedChatlistInvite"
description: "Info about an exported chat folder deep link »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_exportedChatlistInvite.html
---
# Constructor: chatlists.exportedChatlistInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an exported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|filter|[DialogFilter](/API_docs/types/DialogFilter.html) | Yes|Folder ID|
|invite|[ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html) | Yes|The exported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).|



### Type: [chatlists.ExportedChatlistInvite](/API_docs/types/chatlists.ExportedChatlistInvite.html)


### Example:

```
$chatlists_exportedChatlistInvite = ['_' => 'chatlists.exportedChatlistInvite', 'filter' => DialogFilter, 'invite' => ExportedChatlistInvite];
```  
