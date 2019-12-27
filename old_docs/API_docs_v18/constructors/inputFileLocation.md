---
title: inputFileLocation
description: DEPRECATED location of a photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileLocation  
[Back to constructors index](index.md)



DEPRECATED location of a photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|volume\_id|[long](../types/long.md) | Yes|Server volume|
|local\_id|[int](../types/int.md) | Yes|File identifier|
|secret|[long](../types/long.md) | Yes|Check sum to access the file|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputFileLocation = ['_' => 'inputFileLocation', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
inputFileLocation={_='inputFileLocation', volume_id=long, local_id=int, secret=long}

```


