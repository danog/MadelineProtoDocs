---
title: "attachMenuBotIcon"
description: "Represents an attachment menu icon for bot mini apps »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBotIcon  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an attachment menu icon for [bot mini apps »](https://core.telegram.org/api/bots/attach)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|One of the following values: note that animated icons must be played when the user clicks on the button, activating the bot mini app. <br><br>`default_static` \- Default attachment menu icon in SVG format <br>`placeholder_static` \- Default placeholder for opened Web Apps in SVG format <br>`ios_static` \- Attachment menu icon in SVG format for the official iOS app <br>`ios_animated` \- Animated attachment menu icon in TGS format for the official iOS app <br>`android_animated` \- Animated attachment menu icon in TGS format for the official Android app <br>`macos_animated` \- Animated attachment menu icon in TGS format for the official native Mac OS app <br>`ios_side_menu_static` \- Side menu icon in PNG format for the official iOS app <br>`android_side_menu_static` \- Side menu icon in SVG format for the official android app <br>`macos_side_menu_static` \- Side menu icon in PNG format for the official native Mac OS app|
|icon|[Document](/API_docs/types/Document.html) | Optional|The actual icon file.|
|colors|Array of [AttachMenuBotIconColor](/API_docs/types/AttachMenuBotIconColor.html) | Optional|Attachment menu icon colors.|



### Type: [AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html)


### Example:

```
$attachMenuBotIcon = ['_' => 'attachMenuBotIcon', 'name' => 'string', 'icon' => Document, 'colors' => [AttachMenuBotIconColor, AttachMenuBotIconColor]];
```  
