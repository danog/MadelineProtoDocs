---
title: messages.dialogsNotModified
description: Dialogs haven't changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.dialogsNotModified  
[Back to constructors index](index.md)



Dialogs haven't changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Number of dialogs found server-side by the query|



### Type: [messages\_Dialogs](../types/messages_Dialogs.md)


### Example:

```php
$messages_dialogsNotModified = ['_' => 'messages.dialogsNotModified', 'count' => int];
```  


Or, if you're into Lua:

```lua
messages_dialogsNotModified={_='messages.dialogsNotModified', count=int}

```


