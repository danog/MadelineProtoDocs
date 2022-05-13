---
title: "keyboardButtonUserProfile"
description: "Button that links directly to a user profile"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonUserProfile  
[Back to constructors index](/API_docs/constructors/index.html)



Button that links directly to a user profile

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonUserProfile = ['_' => 'keyboardButtonUserProfile', 'text' => 'string', 'user_id' => long];
```  
