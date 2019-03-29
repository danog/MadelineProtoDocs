---
title: inputGameID
description: Game ID
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameID  
[Back to constructors index](index.md)



Game ID

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputGame](../types/InputGame.md)


### Example:

```php
$inputGameID = ['_' => 'inputGameID', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputGameID={_='inputGameID', id=long, access_hash=long}

```


