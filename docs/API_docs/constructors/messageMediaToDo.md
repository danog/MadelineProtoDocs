---
title: "messageMediaToDo"
description: "Represents a todo list »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaToDo  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [todo list »](https://core.telegram.org/api/todo).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|todo|[TodoList](/API_docs/types/TodoList.html) | Yes|The todo list.|
|completions|Array of [TodoCompletion](/API_docs/types/TodoCompletion.html) | Optional|Completed items.|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaToDo = ['_' => 'messageMediaToDo', 'todo' => TodoList, 'completions' => [TodoCompletion, TodoCompletion]];
```  
