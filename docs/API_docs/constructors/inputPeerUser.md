---
title: "inputPeerUser"
description: "Defines a user for further interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerUser  
[Back to constructors index](index.md)



Defines a user for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** value from the [user](../constructors/user.md) constructor|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerUser = ['_' => 'inputPeerUser', 'user_id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputPeerUser={_='inputPeerUser', user_id=long, access_hash=long}

```


