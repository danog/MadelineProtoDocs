# messageActionTodoAppendTasks

> Items were appended to the todo list ».

[Back to constructors index](/API_docs/constructors/index.html)



Items were appended to the [todo list »](https://core.telegram.org/api/todo).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|list|Array of [TodoItem](/API_docs/types/TodoItem.html) | Yes|Appended items.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTodoAppendTasks = ['_' => 'messageActionTodoAppendTasks', 'list' => [TodoItem, TodoItem]];
```
