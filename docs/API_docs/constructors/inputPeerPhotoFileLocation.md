---
title: inputPeerPhotoFileLocation
description: Profile picture location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerPhotoFileLocation  
[Back to constructors index](index.md)



Profile picture location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|big|[Bool](../types/Bool.md) | Optional|Big?|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputPeerPhotoFileLocation = ['_' => 'inputPeerPhotoFileLocation', 'big' => Bool, 'peer' => InputPeer, 'volume_id' => long, 'local_id' => int];
```  


Or, if you're into Lua:

```lua
inputPeerPhotoFileLocation={_='inputPeerPhotoFileLocation', big=Bool, peer=InputPeer, volume_id=long, local_id=int}

```


