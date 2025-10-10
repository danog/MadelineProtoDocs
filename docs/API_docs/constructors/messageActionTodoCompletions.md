---
title: "messageActionTodoCompletions"
description: "Items were marked as completed or not completed in a todo list »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionTodoCompletions  
[Back to constructors index](/API_docs/constructors/index.html)



Items were marked as completed or not completed in a [todo list »](https://core.telegram.org/api/todo).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|completed|Array of [int](/API_docs/types/int.html) | Yes|Items marked as completed.|
|incompleted|Array of [int](/API_docs/types/int.html) | Yes|Items marked as not completed.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTodoCompletions = ['_' => 'messageActionTodoCompletions', 'completed' => [int, int], 'incompleted' => [int, int]];
```  
