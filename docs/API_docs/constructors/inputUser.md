---
title: "inputUser"
description: "Defines a user for further interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUser  
[Back to constructors index](index.md)



Defines a user for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** value from the [user](../constructors/user.md) constructor|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUser = ['_' => 'inputUser', 'user_id' => long, 'access_hash' => long];
```  
