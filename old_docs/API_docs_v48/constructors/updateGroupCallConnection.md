---
title: updateGroupCallConnection
description: updateGroupCallConnection attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallConnection  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|presentation|[Bool](../types/Bool.md) | Optional|
|params|[DataJSON](../types/DataJSON.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGroupCallConnection = ['_' => 'updateGroupCallConnection', 'presentation' => Bool, 'params' => DataJSON];
```  


Or, if you're into Lua:

```lua
updateGroupCallConnection={_='updateGroupCallConnection', presentation=Bool, params=DataJSON}

```


