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
|title\_noanimate|[Bool](/API_docs/types/Bool.html) | Optional|If set, any animated emojis present in `title` should not be animated and should be instead frozen on the first frame.|
|id|[int](/API_docs/types/int.html) | Yes|ID of the folder|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Name of the folder (max 12 UTF-8 chars)|
|emoticon|[string](/API_docs/types/string.html) | Optional|Emoji to use as icon for the folder.|
|color|[int](/API_docs/types/int.html) | Optional|A color ID for the [folder tag associated to this folder, see here »](https://core.telegram.org/api/folders#folder-tags) for more info.|
|pinned\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Pinned chats, [folders](https://core.telegram.org/api/folders) can have unlimited pinned chats|
|include\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Chats to include in the folder|



### Type: [DialogFilter](/API_docs/types/DialogFilter.html)


### Example:

```
$dialogFilterChatlist = ['_' => 'dialogFilterChatlist', 'has_my_invites' => Bool, 'title_noanimate' => Bool, 'id' => int, 'title' => TextWithEntities, 'emoticon' => 'string', 'color' => int, 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer]];
```  
