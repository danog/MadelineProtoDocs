---
title: inputUserForeign
description: User foreign
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUserForeign  
[Back to constructors index](index.md)



User foreign

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUserForeign = ['_' => 'inputUserForeign', 'user_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputUserForeign", "user_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputUserForeign={_='inputUserForeign', user_id=int, access_hash=long}

```


