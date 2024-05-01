---
title: "messages.searchResultsPositions"
description: "Information about sparse positions of messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsPositions.html
---
# Constructor: messages.searchResultsPositions  
[Back to constructors index](/API_docs/constructors/index.html)



Information about sparse positions of messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of found messages|
|positions|Array of [SearchResultsPosition](/API_docs/types/SearchResultsPosition.html) | Yes|List of message positions|



### Type: [messages.SearchResultsPositions](/API_docs/types/messages.SearchResultsPositions.html)


### Example:

```
$messages_searchResultsPositions = ['_' => 'messages.searchResultsPositions', 'count' => int, 'positions' => [SearchResultsPosition, SearchResultsPosition]];
```  
