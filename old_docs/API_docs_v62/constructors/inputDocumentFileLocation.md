---
title: inputDocumentFileLocation
description: Document location (video, voice, audio, basically every type except photo)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocumentFileLocation  
[Back to constructors index](index.md)



Document location (video, voice, audio, basically every type except photo)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|
|version|[int](../types/int.md) | Yes|Version|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputDocumentFileLocation = ['_' => 'inputDocumentFileLocation', 'id' => long, 'access_hash' => long, 'version' => int];
```  


Or, if you're into Lua:

```lua
inputDocumentFileLocation={_='inputDocumentFileLocation', id=long, access_hash=long, version=int}

```


