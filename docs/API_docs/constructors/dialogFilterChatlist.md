---
title: "dialogFilterChatlist"
description: "A folder imported using a chat folder deep link »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilterChatlist  
[Back to constructors index](/API_docs/constructors/index.html)



A folder imported using a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_my\_invites|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user has created some [chat folder deep links »](https://core.telegram.org/api/links#chat-folder-links) to share the folder as well.|
|id|[int](/API_docs/types/int.html) | Yes|ID of the folder|
|title|[string](/API_docs/types/string.html) | Yes|Name of the folder|
|emoticon|[string](/API_docs/types/string.html) | Optional|Emoji to use as icon for the folder.|
|color|[int](/API_docs/types/int.html) | Optional|
|pinned\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Pinned chats, [folders](https://core.telegram.org/api/folders) can have unlimited pinned chats|
|include\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Chats to include in the folder|



### Type: [DialogFilter](/API_docs/types/DialogFilter.html)


### Example:

```
$dialogFilterChatlist = ['_' => 'dialogFilterChatlist', 'has_my_invites' => Bool, 'id' => int, 'title' => 'string', 'emoticon' => 'string', 'color' => int, 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer]];
```  
