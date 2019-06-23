---
title: fileLocationUnavailable
description: File location unavailable
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileLocationUnavailable\_23  
[Back to constructors index](index.md)



File location unavailable

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|
|secret|[long](../types/long.md) | Yes|Secret|



### Type: [FileLocation](../types/FileLocation.md)


### Example:

```php
$fileLocationUnavailable_23 = ['_' => 'fileLocationUnavailable', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
fileLocationUnavailable_23={_='fileLocationUnavailable', volume_id=long, local_id=int, secret=long}

```


