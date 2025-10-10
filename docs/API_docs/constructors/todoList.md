---
title: "todoList"
description: "Represents a todo list »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: todoList  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [todo list »](https://core.telegram.org/api/todo).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|others\_can\_append|[Bool](/API_docs/types/Bool.html) | Optional|If set, users different from the creator of the list can append items to the list.|
|others\_can\_complete|[Bool](/API_docs/types/Bool.html) | Optional|If set, users different from the creator of the list can complete items in the list.|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Title of the todo list, maximum length equal to [todo\_title\_length\_max »](https://core.telegram.org/api/config#todo-title-length-max).|
|list|Array of [TodoItem](/API_docs/types/TodoItem.html) | Yes|Items of the list.|



### Type: [TodoList](/API_docs/types/TodoList.html)


### Example:

```
$todoList = ['_' => 'todoList', 'others_can_append' => Bool, 'others_can_complete' => Bool, 'title' => TextWithEntities, 'list' => [TodoItem, TodoItem]];
```  
