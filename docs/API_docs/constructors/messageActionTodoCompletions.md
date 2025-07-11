---
title: "messageActionTodoCompletions"
description: "messageActionTodoCompletions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionTodoCompletions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|completed|Array of [int](/API_docs/types/int.html) | Yes|
|incompleted|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTodoCompletions = ['_' => 'messageActionTodoCompletions', 'completed' => [int, int], 'incompleted' => [int, int]];
```  
