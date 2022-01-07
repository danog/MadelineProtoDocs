---
title: "updates.state"
description: "Updates state."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_state.html
---
# Constructor: updates.state  
[Back to constructors index](index.md)



Updates state.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|Number of events occured in a text box|
|qts|[int](../types/int.md) | Yes|Position in a sequence of updates in secret chats. For further detailes refer to article [secret chats](https://core.telegram.org/api/end-to-end)<br>Parameter was added in [eigth layer](https://core.telegram.org/api/layers#layer-8).|
|date|[int](../types/int.md) | Yes|Date of condition|
|seq|[int](../types/int.md) | Yes|Number of sent updates|
|unread\_count|[int](../types/int.md) | Yes|Number of unread messages|



### Type: [updates.State](../types/updates.State.md)


### Example:

```php
$updates_state = ['_' => 'updates.state', 'pts' => int, 'qts' => int, 'date' => int, 'seq' => int, 'unread_count' => int];
```  
