---
title: "community"
description: "community attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: community  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|
|left|[Bool](/API_docs/types/Bool.html) | Optional|
|min|[Bool](/API_docs/types/Bool.html) | Optional|
|collapsed\_in\_dialogs|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|access\_hash|[long](/API_docs/types/long.html) | Optional|
|title|[string](/API_docs/types/string.html) | Yes|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Optional|



### Type: [Chat](/API_docs/types/Chat.html)


### Example:

```
$community = ['_' => 'community', 'creator' => Bool, 'left' => Bool, 'min' => Bool, 'collapsed_in_dialogs' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'photo' => ChatPhoto, 'date' => int, 'admin_rights' => ChatAdminRights, 'default_banned_rights' => ChatBannedRights];
```  
