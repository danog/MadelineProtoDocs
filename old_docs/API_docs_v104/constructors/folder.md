---
title: folder
description: Folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: folder  
[Back to constructors index](index.md)



Folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autofill\_new\_broadcasts|[Bool](../types/Bool.md) | Optional|Automatically add new channels to this folder|
|autofill\_public\_groups|[Bool](../types/Bool.md) | Optional|Automatically add joined new public supergroups to this folder|
|autofill\_new\_correspondents|[Bool](../types/Bool.md) | Optional|Automatically add new private chats to this folder|
|id|[int](../types/int.md) | Yes|Folder ID|
|title|[string](../types/string.md) | Yes|Folder title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Folder picture|



### Type: [Folder](../types/Folder.md)


### Example:

```php
$folder = ['_' => 'folder', 'autofill_new_broadcasts' => Bool, 'autofill_public_groups' => Bool, 'autofill_new_correspondents' => Bool, 'id' => int, 'title' => 'string', 'photo' => ChatPhoto];
```  


Or, if you're into Lua:

```lua
folder={_='folder', autofill_new_broadcasts=Bool, autofill_public_groups=Bool, autofill_new_correspondents=Bool, id=int, title='string', photo=ChatPhoto}

```


