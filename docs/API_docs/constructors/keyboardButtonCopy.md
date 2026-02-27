---
title: "keyboardButtonCopy"
description: "Clipboard button: when clicked, the attached text must be copied to the clipboard."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonCopy  
[Back to constructors index](/API_docs/constructors/index.html)



Clipboard button: when clicked, the attached text must be copied to the clipboard.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|style|[KeyboardButtonStyle](/API_docs/types/KeyboardButtonStyle.html) | Optional|
|text|[string](/API_docs/types/string.html) | Yes|Title of the button|
|copy\_text|[string](/API_docs/types/string.html) | Yes|The text that will be copied to the clipboard|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonCopy = ['_' => 'keyboardButtonCopy', 'style' => KeyboardButtonStyle, 'text' => 'string', 'copy_text' => 'string'];
```  
