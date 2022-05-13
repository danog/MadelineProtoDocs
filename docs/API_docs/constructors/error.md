---
title: "error"
description: "Error."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: error  
[Back to constructors index](/API_docs/constructors/index.html)



Error.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|code|[int](/API_docs/types/int.html) | Yes|Error code|
|text|[string](/API_docs/types/string.html) | Yes|Message|



### Type: [Error](/API_docs/types/Error.html)


### Example:

```
$error = ['_' => 'error', 'code' => int, 'text' => 'string'];
```  
