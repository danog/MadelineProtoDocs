---
title: messages.messagesNotModified
description: No new messages matching the query were found
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.messagesNotModified  
[Back to constructors index](index.md)



No new messages matching the query were found

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Number of results found server-side by the given query|



### Type: [messages\_Messages](../types/messages_Messages.md)


### Example:

```php
$messages_messagesNotModified = ['_' => 'messages.messagesNotModified', 'count' => int];
```  


Or, if you're into Lua:

```lua
messages_messagesNotModified={_='messages.messagesNotModified', count=int}

```


