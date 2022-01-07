---
title: "help.support"
description: "Info on support user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_support.html
---
# Constructor: help.support  
[Back to constructors index](/API_docs/constructors/index.md)



Info on support user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.md) | Yes|Phone number|
|user|[User](/API_docs/types/User.md) | Optional|User|



### Type: [help.Support](/API_docs/types/help.Support.md)


### Example:

```php
$help_support = ['_' => 'help.support', 'phone_number' => 'string', 'user' => User];
```  
