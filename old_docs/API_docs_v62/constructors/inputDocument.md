---
title: inputDocument
description: Document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocument  
[Back to constructors index](index.md)



Document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputDocument](../types/InputDocument.md)


### Example:

```php
$inputDocument = ['_' => 'inputDocument', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputDocument={_='inputDocument', id=long, access_hash=long}

```


