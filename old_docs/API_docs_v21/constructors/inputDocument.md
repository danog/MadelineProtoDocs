---
title: inputDocument
description: Defines a video for subsequent interaction.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocument  
[Back to constructors index](index.md)



Defines a video for subsequent interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|



### Type: [InputDocument](../types/InputDocument.md)


### Example:

```php
$inputDocument = ['_' => 'inputDocument', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputDocument={_='inputDocument', id=long, access_hash=long}

```


