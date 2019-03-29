---
title: inputGeoChat
description: Geo chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGeoChat  
[Back to constructors index](index.md)



Geo chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputGeoChat](../types/InputGeoChat.md)


### Example:

```php
$inputGeoChat = ['_' => 'inputGeoChat', 'chat_id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputGeoChat={_='inputGeoChat', chat_id=int, access_hash=long}

```


