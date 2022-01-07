---
title: "error"
description: "Error."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: error  
[Back to constructors index](/API_docs/constructors/index.md)



Error.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|code|[int](/API_docs/types/int.md) | Yes|Error code|
|text|[string](/API_docs/types/string.md) | Yes|Message|



### Type: [Error](/API_docs/types/Error.md)


### Example:

```php
$error = ['_' => 'error', 'code' => int, 'text' => 'string'];
```  
