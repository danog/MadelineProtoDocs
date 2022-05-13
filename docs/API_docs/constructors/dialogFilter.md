---
title: "dialogFilter"
description: "Dialog filter AKA folder"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilter  
[Back to constructors index](/API_docs/constructors/index.html)



Dialog filter AKA [folder](https://core.telegram.org/api/folders)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|Whether to include all contacts in this [folder](https://core.telegram.org/api/folders)|
|non\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|Whether to include all non-contacts in this [folder](https://core.telegram.org/api/folders)|
|groups|[Bool](/API_docs/types/Bool.html) | Optional|Whether to include all groups in this [folder](https://core.telegram.org/api/folders)|
|broadcasts|[Bool](/API_docs/types/Bool.html) | Optional|Whether to include all channels in this [folder](https://core.telegram.org/api/folders)|
|bots|[Bool](/API_docs/types/Bool.html) | Optional|Whether to include all bots in this [folder](https://core.telegram.org/api/folders)|
|exclude\_muted|[Bool](/API_docs/types/Bool.html) | Optional|Whether to exclude muted chats from this [folder](https://core.telegram.org/api/folders)|
|exclude\_read|[Bool](/API_docs/types/Bool.html) | Optional|Whether to exclude read chats from this [folder](https://core.telegram.org/api/folders)|
|exclude\_archived|[Bool](/API_docs/types/Bool.html) | Optional|Whether to exclude archived chats from this [folder](https://core.telegram.org/api/folders)|
|id|[int](/API_docs/types/int.html) | Yes|[Folder](https://core.telegram.org/api/folders) ID|
|title|[string](/API_docs/types/string.html) | Yes|[Folder](https://core.telegram.org/api/folders) name|
|emoticon|[string](/API_docs/types/string.html) | Optional|[Folder](https://core.telegram.org/api/folders) emoticon|
|pinned\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Pinned chats, [folders](https://core.telegram.org/api/folders) can have unlimited pinned chats|
|include\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Include the following chats in this [folder](https://core.telegram.org/api/folders)|
|exclude\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|Exclude the following chats from this [folder](https://core.telegram.org/api/folders)|



### Type: [DialogFilter](/API_docs/types/DialogFilter.html)


### Example:

```
$dialogFilter = ['_' => 'dialogFilter', 'contacts' => Bool, 'non_contacts' => Bool, 'groups' => Bool, 'broadcasts' => Bool, 'bots' => Bool, 'exclude_muted' => Bool, 'exclude_read' => Bool, 'exclude_archived' => Bool, 'id' => int, 'title' => 'string', 'emoticon' => 'string', 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer], 'exclude_peers' => [InputPeer, InputPeer]];
```  
