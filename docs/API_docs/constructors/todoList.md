---
title: "todoList"
description: "todoList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: todoList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|others\_can\_append|[Bool](/API_docs/types/Bool.html) | Optional|
|others\_can\_complete|[Bool](/API_docs/types/Bool.html) | Optional|
|title|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|
|list|Array of [TodoItem](/API_docs/types/TodoItem.html) | Yes|



### Type: [TodoList](/API_docs/types/TodoList.html)


### Example:

```
$todoList = ['_' => 'todoList', 'others_can_append' => Bool, 'others_can_complete' => Bool, 'title' => TextWithEntities, 'list' => [TodoItem, TodoItem]];
```  
