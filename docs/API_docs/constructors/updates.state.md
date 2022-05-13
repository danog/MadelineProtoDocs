---
title: "updates.state"
description: "Updates state."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_state.html
---
# Constructor: updates.state  
[Back to constructors index](/API_docs/constructors/index.html)



Updates state.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](/API_docs/types/int.html) | Yes|Number of events occurred in a text box|
|qts|[int](/API_docs/types/int.html) | Yes|Position in a sequence of updates in secret chats. For further details refer to article [secret chats](https://core.telegram.org/api/end-to-end)|
|date|[int](/API_docs/types/int.html) | Yes|Date of condition|
|seq|[int](/API_docs/types/int.html) | Yes|Number of sent updates|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages|



### Type: [updates.State](/API_docs/types/updates.State.html)


### Example:

```
$updates_state = ['_' => 'updates.state', 'pts' => int, 'qts' => int, 'date' => int, 'seq' => int, 'unread_count' => int];
```  
