---
title: "inputFolderPeer"
description: "Peer in a folder"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFolderPeer  
[Back to constructors index](index.md)



Peer in a folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|
|folder\_id|[int](../types/int.md) | Yes|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|



### Type: [InputFolderPeer](../types/InputFolderPeer.md)


### Example:

```php
$inputFolderPeer = ['_' => 'inputFolderPeer', 'peer' => InputPeer, 'folder_id' => int];
```  
