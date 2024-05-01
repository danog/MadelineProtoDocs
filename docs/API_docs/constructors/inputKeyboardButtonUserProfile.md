---
title: "inputKeyboardButtonUserProfile"
description: "Button that links directly to a user profile"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputKeyboardButtonUserProfile  
[Back to constructors index](/API_docs/constructors/index.html)



Button that links directly to a user profile

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|user\_id|[InputUser](/API_docs/types/InputUser.html) | Optional|User ID|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$inputKeyboardButtonUserProfile = ['_' => 'inputKeyboardButtonUserProfile', 'text' => 'string', 'user_id' => InputUser];
```  
