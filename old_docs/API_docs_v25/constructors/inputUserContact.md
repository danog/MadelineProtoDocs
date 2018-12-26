---
title: inputUserContact
description: User contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUserContact  
[Back to constructors index](index.md)



User contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUserContact = ['_' => 'inputUserContact', 'user_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputUserContact", "user_id": int}
```


Or, if you're into Lua:

```lua
inputUserContact={_='inputUserContact', user_id=int}

```


