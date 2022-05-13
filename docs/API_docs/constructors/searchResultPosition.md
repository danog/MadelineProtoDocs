---
title: "searchResultPosition"
description: "Information about a message in a specific position"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: searchResultPosition  
[Back to constructors index](/API_docs/constructors/index.html)



Information about a message in a specific position

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|date|[int](/API_docs/types/int.html) | Yes|When was the message sent|
|offset|[int](/API_docs/types/int.html) | Yes|0-based message position in the full list of suitable messages|



### Type: [SearchResultsPosition](/API_docs/types/SearchResultsPosition.html)


### Example:

```
$searchResultPosition = ['_' => 'searchResultPosition', 'msg_id' => int, 'date' => int, 'offset' => int];
```  
