---
title: "attachMenuBotIconColor"
description: "Represents an attachment menu icon color for bot web apps »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBotIconColor  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an attachment menu icon color for [bot web apps »](https://core.telegram.org/api/bots/attach)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|One of the following values: <br>`light_icon` \- Color of the attachment menu icon (light mode) <br>`light_text` \- Color of the attachment menu label, once selected (light mode) <br>`dark_icon` \- Color of the attachment menu icon (dark mode) <br>`dark_text` \- Color of the attachment menu label, once selected (dark mode)|
|color|[int](/API_docs/types/int.html) | Yes|Color in RGB24 format|



### Type: [AttachMenuBotIconColor](/API_docs/types/AttachMenuBotIconColor.html)


### Example:

```
$attachMenuBotIconColor = ['_' => 'attachMenuBotIconColor', 'name' => 'string', 'color' => int];
```  
