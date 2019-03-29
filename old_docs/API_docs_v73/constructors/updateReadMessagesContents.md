---
title: updateReadMessagesContents
description: Update read messages contents
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadMessagesContents  
[Back to constructors index](index.md)



Update read messages contents

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](../types/int.md) | Yes|Messages|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadMessagesContents = ['_' => 'updateReadMessagesContents', 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateReadMessagesContents={_='updateReadMessagesContents', messages={int}, pts=int, pts_count=int}

```


