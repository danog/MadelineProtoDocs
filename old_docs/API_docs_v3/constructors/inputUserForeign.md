---
title: inputUserForeign
description: inputUserForeign attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUserForeign  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUserForeign = ['_' => 'inputUserForeign', 'user_id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputUserForeign={_='inputUserForeign', user_id=int, access_hash=long}

```


