---
title: updateReadMessagesContents
description: Contents of messages in the common [message box](https://core.telegram.org/api/updates) were read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadMessagesContents  
[Back to constructors index](index.md)



Contents of messages in the common [message box](https://core.telegram.org/api/updates) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](../types/int.md) | Yes|IDs of read messages|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadMessagesContents = ['_' => 'updateReadMessagesContents', 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateReadMessagesContents={_='updateReadMessagesContents', messages={int}, pts=int, pts_count=int}

```


