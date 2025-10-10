---
title: "todoItem"
description: "An item of a todo list »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: todoItem  
[Back to constructors index](/API_docs/constructors/index.html)



An item of a [todo list »](https://core.telegram.org/api/todo).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|ID of the item, a positive (non-zero) integer unique within the current list.|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Text of the item, maximum length equal to [todo\_item\_length\_max »](https://core.telegram.org/api/config#todo-item-length-max).|



### Type: [TodoItem](/API_docs/types/TodoItem.html)


### Example:

```
$todoItem = ['_' => 'todoItem', 'id' => int, 'title' => TextWithEntities];
```  
