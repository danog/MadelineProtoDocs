---
title: "fileLocationUnavailable"
description: "fileLocationUnavailable attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileLocationUnavailable\_23  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|volume\_id|[long](../types/long.md) | Yes|
|local\_id|[int](../types/int.md) | Yes|
|secret|[long](../types/long.md) | Yes|



### Type: [FileLocation](../types/FileLocation.md)


### Example:

```php
$fileLocationUnavailable_23 = ['_' => 'fileLocationUnavailable', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
fileLocationUnavailable_23={_='fileLocationUnavailable', volume_id=long, local_id=int, secret=long}

```


