---
title: "documentAttributeCustomEmoji"
description: "Info about a custom emoji"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeCustomEmoji  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a custom emoji

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|free|[Bool](/API_docs/types/Bool.html) | Optional|Whether this custom emoji can be sent by non-Premium users|
|text\_color|[Bool](/API_docs/types/Bool.html) | Optional|Whether the color of this TGS custom emoji should be changed to the text color when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context.|
|alt|[string](/API_docs/types/string.html) | Yes|The actual emoji|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|The emoji stickerset to which this emoji belongs.|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.html)


### Example:

```
$documentAttributeCustomEmoji = ['_' => 'documentAttributeCustomEmoji', 'free' => Bool, 'text_color' => Bool, 'alt' => 'string', 'stickerset' => InputStickerSet];
```  
