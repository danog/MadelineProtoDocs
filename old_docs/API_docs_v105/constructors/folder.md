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
|autofill\_new\_broadcasts|[Bool](../types/Bool.md) | Optional|New broadcasts?|
|autofill\_public\_groups|[Bool](../types/Bool.md) | Optional|Autofill public groups?|
|autofill\_new\_correspondents|[Bool](../types/Bool.md) | Optional|New correspondents|
|id|[int](../types/int.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|



### Type: [Folder](../types/Folder.md)


### Example:

```php
$folder = ['_' => 'folder', 'autofill_new_broadcasts' => Bool, 'autofill_public_groups' => Bool, 'autofill_new_correspondents' => Bool, 'id' => int, 'title' => 'string', 'photo' => ChatPhoto];
```  


Or, if you're into Lua:

```lua
folder={_='folder', autofill_new_broadcasts=Bool, autofill_public_groups=Bool, autofill_new_correspondents=Bool, id=int, title='string', photo=ChatPhoto}

```


