---
title: "messages.searchResultsPositions"
description: "messages.searchResultsPositions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsPositions.html
---
# Constructor: messages.searchResultsPositions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|positions|Array of [SearchResultsPosition](/API_docs/types/SearchResultsPosition.html) | Yes|



### Type: [messages.SearchResultsPositions](/API_docs/types/messages.SearchResultsPositions.html)


### Example:

```php
$messages_searchResultsPositions = ['_' => 'messages.searchResultsPositions', 'count' => int, 'positions' => [SearchResultsPosition, SearchResultsPosition]];
```  
