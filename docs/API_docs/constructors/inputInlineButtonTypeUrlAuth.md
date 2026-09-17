---
title: "inputInlineButtonTypeUrlAuth"
description: "inputInlineButtonTypeUrlAuth attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInlineButtonTypeUrlAuth  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|
|fwd\_text|[string](/API_docs/types/string.html) | Optional|
|url|[string](/API_docs/types/string.html) | Yes|
|bot|[InputUser](/API_docs/types/InputUser.html) | Optional|



### Type: [InlineButtonType](/API_docs/types/InlineButtonType.html)


### Example:

```
$inputInlineButtonTypeUrlAuth = ['_' => 'inputInlineButtonTypeUrlAuth', 'request_write_access' => Bool, 'fwd_text' => 'string', 'url' => 'string', 'bot' => InputUser];
```  
