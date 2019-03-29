---
title: inputFileLocation
description: File location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileLocation  
[Back to constructors index](index.md)



File location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|
|secret|[long](../types/long.md) | Yes|Secret|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputFileLocation = ['_' => 'inputFileLocation', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
inputFileLocation={_='inputFileLocation', volume_id=long, local_id=int, secret=long}

```


