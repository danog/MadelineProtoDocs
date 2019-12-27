---
title: inputFolderPeer
description: Peer in a folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFolderPeer  
[Back to constructors index](index.md)



Peer in a folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|
|folder\_id|[int](../types/int.md) | Yes|Folder ID|



### Type: [InputFolderPeer](../types/InputFolderPeer.md)


### Example:

```php
$inputFolderPeer = ['_' => 'inputFolderPeer', 'peer' => InputPeer, 'folder_id' => int];
```  


Or, if you're into Lua:

```lua
inputFolderPeer={_='inputFolderPeer', peer=InputPeer, folder_id=int}

```


