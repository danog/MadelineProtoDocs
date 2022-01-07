---
title: "messages.searchCounter"
description: "Indicates how many results would be found by a messages.search call with the same parameters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchCounter.html
---
# Constructor: messages.searchCounter  
[Back to constructors index](/API_docs/constructors/index.md)



Indicates how many results would be found by a [messages.search](../methods/messages.search.md) call with the same parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](/API_docs/types/Bool.md) | Optional|If set, the results may be inexact|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.md) | Yes|Provided message filter|
|count|[int](/API_docs/types/int.md) | Yes|Number of results that were found server-side|



### Type: [messages.SearchCounter](/API_docs/types/messages.SearchCounter.md)


### Example:

```php
$messages_searchCounter = ['_' => 'messages.searchCounter', 'inexact' => Bool, 'filter' => MessagesFilter, 'count' => int];
```  
