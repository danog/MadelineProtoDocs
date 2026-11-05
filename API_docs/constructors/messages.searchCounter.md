# messages.searchCounter

> Indicates how many results would be found by a messages.search call with the same parameters

[Back to constructors index](/API_docs/constructors/index.html)



Indicates how many results would be found by a [messages.search](../methods/messages.search.html) call with the same parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](/API_docs/types/Bool.html) | Optional|If set, the results may be inexact|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Yes|Provided message filter|
|count|[int](/API_docs/types/int.html) | Yes|Number of results that were found server-side|



### Type: [messages.SearchCounter](/API_docs/types/messages.SearchCounter.html)


### Example:

```
$messages_searchCounter = ['_' => 'messages.searchCounter', 'inexact' => Bool, 'filter' => MessagesFilter, 'count' => int];
```
