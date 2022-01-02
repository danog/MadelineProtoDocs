---
title: "messages.searchCounter"
description: "Indicates how many results would be found by a messages.search call with the same parameters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchCounter.html
---
# Constructor: messages.searchCounter  
[Back to constructors index](index.md)



Indicates how many results would be found by a [messages.search](../methods/messages.search.md) call with the same parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|If set, the results may be inexact|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Yes|Provided message filter|
|count|[int](../types/int.md) | Yes|Number of results that were found server-side|



### Type: [messages.SearchCounter](../types/messages.SearchCounter.md)


### Example:

```php
$messages_searchCounter = ['_' => 'messages.searchCounter', 'inexact' => Bool, 'filter' => MessagesFilter, 'count' => int];
```  


Or, if you're into Lua:

```lua
messages_searchCounter={_='messages.searchCounter', inexact=Bool, filter=MessagesFilter, count=int}

```


