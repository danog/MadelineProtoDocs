---
title: "keyboardButtonRequestPoll"
description: "A button that allows the user to create and send a poll when pressed; available only in private"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRequestPoll  
[Back to constructors index](/API_docs/constructors/index.html)



A button that allows the user to create and send a poll when pressed; available only in private

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|quiz|[Bool](/API_docs/types/Bool.html) | Optional|If set, only quiz polls can be sent|
|text|[string](/API_docs/types/string.html) | Yes|Button text|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonRequestPoll = ['_' => 'keyboardButtonRequestPoll', 'quiz' => Bool, 'text' => 'string'];
```  
