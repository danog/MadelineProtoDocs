---
title: messages.searchCounter
description: Search counter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.searchCounter  
[Back to constructors index](index.md)



Search counter

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|Inexact?|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Yes|Filter|
|count|[int](../types/int.md) | Yes|Count|



### Type: [messages\_SearchCounter](../types/messages_SearchCounter.md)


### Example:

```php
$messages_searchCounter = ['_' => 'messages.searchCounter', 'inexact' => Bool, 'filter' => MessagesFilter, 'count' => int];
```  


Or, if you're into Lua:

```lua
messages_searchCounter={_='messages.searchCounter', inexact=Bool, filter=MessagesFilter, count=int}

```


