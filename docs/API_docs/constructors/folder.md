---
title: "folder"
description: "Folder"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: folder  
[Back to constructors index](/API_docs/constructors/index.md)



Folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autofill\_new\_broadcasts|[Bool](/API_docs/types/Bool.md) | Optional|Automatically add new channels to this folder|
|autofill\_public\_groups|[Bool](/API_docs/types/Bool.md) | Optional|Automatically add joined new public supergroups to this folder|
|autofill\_new\_correspondents|[Bool](/API_docs/types/Bool.md) | Optional|Automatically add new private chats to this folder|
|id|[int](/API_docs/types/int.md) | Yes|Folder ID|
|title|[string](/API_docs/types/string.md) | Yes|Folder title|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.md) | Optional|Folder picture|



### Type: [Folder](/API_docs/types/Folder.md)


### Example:

```php
$folder = ['_' => 'folder', 'autofill_new_broadcasts' => Bool, 'autofill_public_groups' => Bool, 'autofill_new_correspondents' => Bool, 'id' => int, 'title' => 'string', 'photo' => ChatPhoto];
```  
