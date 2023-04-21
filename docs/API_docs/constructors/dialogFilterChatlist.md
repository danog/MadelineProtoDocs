---
title: "dialogFilterChatlist"
description: "dialogFilterChatlist attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilterChatlist  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|has\_my\_invites|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|emoticon|[string](/API_docs/types/string.html) | Optional|
|pinned\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|
|include\_peers|Array of [InputPeer](/API_docs/types/InputPeer.html) | Yes|



### Type: [DialogFilter](/API_docs/types/DialogFilter.html)


### Example:

```
$dialogFilterChatlist = ['_' => 'dialogFilterChatlist', 'has_my_invites' => Bool, 'id' => int, 'title' => 'string', 'emoticon' => 'string', 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer]];
```  
