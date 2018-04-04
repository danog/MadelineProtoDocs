---
title: inputUserContact
description: inputUserContact attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: inputUserContact  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|



### Type: [InputUser](../types/InputUser.md)


### Example:

```
$inputUserContact = ['_' => 'inputUserContact', 'user_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputUserContact", "user_id": int}
```


Or, if you're into Lua:  


```
inputUserContact={_='inputUserContact', user_id=int}

```


