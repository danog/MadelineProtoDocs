---
title: "todoCompletion"
description: "A completed todo list » item."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: todoCompletion  
[Back to constructors index](/API_docs/constructors/index.html)



A completed [todo list »](https://core.telegram.org/api/todo) item.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|The ID of the completed item.|
|completed\_by|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|When was the item completed.|



### Type: [TodoCompletion](/API_docs/types/TodoCompletion.html)


### Example:

```
$todoCompletion = ['_' => 'todoCompletion', 'id' => int, 'completed_by' => Peer, 'date' => int];
```  
