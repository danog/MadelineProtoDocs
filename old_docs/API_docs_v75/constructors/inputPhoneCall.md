---
title: inputPhoneCall
description: inputPhoneCall attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoneCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputPhoneCall](../types/InputPhoneCall.md)


### Example:

```
$inputPhoneCall = ['_' => 'inputPhoneCall', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPhoneCall", "id": long, "access_hash": long}
```


Or, if you're into Lua:  


```
inputPhoneCall={_='inputPhoneCall', id=long, access_hash=long}

```


