---
title: "attachMenuBotIcon"
description: "attachMenuBotIcon attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBotIcon  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name|[string](/API_docs/types/string.html) | Yes|
|icon|[Document](/API_docs/types/Document.html) | Optional|
|colors|Array of [AttachMenuBotIconColor](/API_docs/types/AttachMenuBotIconColor.html) | Optional|



### Type: [AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html)


### Example:

```
$attachMenuBotIcon = ['_' => 'attachMenuBotIcon', 'name' => 'string', 'icon' => Document, 'colors' => [AttachMenuBotIconColor, AttachMenuBotIconColor]];
```  
