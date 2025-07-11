---
title: "messageMediaToDo"
description: "messageMediaToDo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaToDo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|todo|[TodoList](/API_docs/types/TodoList.html) | Yes|
|completions|Array of [TodoCompletion](/API_docs/types/TodoCompletion.html) | Optional|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaToDo = ['_' => 'messageMediaToDo', 'todo' => TodoList, 'completions' => [TodoCompletion, TodoCompletion]];
```  
