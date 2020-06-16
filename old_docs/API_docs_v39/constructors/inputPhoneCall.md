---
title: inputPhoneCall
description: Phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoneCall  
[Back to constructors index](index.md)



Phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Call ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputPhoneCall](../types/InputPhoneCall.md)


### Example:

```php
$inputPhoneCall = ['_' => 'inputPhoneCall', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputPhoneCall={_='inputPhoneCall', id=long, access_hash=long}

```


