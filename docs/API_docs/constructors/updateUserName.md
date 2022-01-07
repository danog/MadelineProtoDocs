---
title: "updateUserName"
description: "Changes the user's first name, last name and username."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserName  
[Back to constructors index](index.md)



Changes the user's first name, last name and username.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|first\_name|[string](../types/string.md) | Yes|New first name. Corresponds to the new value of **real\_first\_name** field of the [userFull](../constructors/userFull.md) constructor.|
|last\_name|[string](../types/string.md) | Yes|New last name. Corresponds to the new value of **real\_last\_name** field of the [userFull](../constructors/userFull.md) constructor.|
|username|[string](../types/string.md) | Yes|New username.<br>Parameter added in [Layer 18](https://core.telegram.org/api/layers#layer-18).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserName = ['_' => 'updateUserName', 'user_id' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string'];
```  
