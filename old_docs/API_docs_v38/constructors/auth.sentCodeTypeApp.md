---
title: auth.sentCodeTypeApp
description: The code was sent through the telegram app
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeApp.html
---
# Constructor: auth.sentCodeTypeApp  
[Back to constructors index](index.md)



The code was sent through the telegram app

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](../types/int.md) | Yes|Length of the code in bytes|



### Type: [auth.SentCodeType](../types/auth.SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeApp = ['_' => 'auth.sentCodeTypeApp', 'length' => int];
```  


Or, if you're into Lua:

```lua
auth_sentCodeTypeApp={_='auth.sentCodeTypeApp', length=int}

```


