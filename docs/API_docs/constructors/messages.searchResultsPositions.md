---
title: "messages.searchResultsPositions"
description: "messages.searchResultsPositions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsPositions.html
---
# Constructor: messages.searchResultsPositions  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|positions|Array of [SearchResultsPosition](../types/SearchResultsPosition.md) | Yes|



### Type: [messages.SearchResultsPositions](../types/messages.SearchResultsPositions.md)


### Example:

```php
$messages_searchResultsPositions = ['_' => 'messages.searchResultsPositions', 'count' => int, 'positions' => [SearchResultsPosition, SearchResultsPosition]];
```  
