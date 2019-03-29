---
title: fileLocation
description: File location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileLocation\_23  
[Back to constructors index](index.md)



File location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|
|secret|[long](../types/long.md) | Yes|Secret|



### Type: [FileLocation](../types/FileLocation.md)


### Example:

```php
$fileLocation_23 = ['_' => 'fileLocation', 'dc_id' => int, 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
fileLocation_23={_='fileLocation', dc_id=int, volume_id=long, local_id=int, secret=long}

```


