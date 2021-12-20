---
title: "webPagePending"
description: "A preview of the webpage is currently being generated"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPagePending  
[Back to constructors index](index.md)



A preview of the webpage is currently being generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID of preview|
|date|[int](../types/int.md) | Yes|When was the processing started|



### Type: [WebPage](../types/WebPage.md)


### Example:

```php
$webPagePending = ['_' => 'webPagePending', 'id' => long, 'date' => int];
```  


Or, if you're into Lua:

```lua
webPagePending={_='webPagePending', id=long, date=int}

```


