---
title: "updateEditMessage"
description: "A message was edited"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditMessage  
[Back to constructors index](index.md)



A message was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|The new edited message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEditMessage = ['_' => 'updateEditMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateEditMessage={_='updateEditMessage', message=Message, pts=int, pts_count=int}

```


