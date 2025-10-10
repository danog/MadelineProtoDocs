---
title: "inputChatThemeUniqueGift"
description: "Set a theme based on an owned collectible gift », returned by account.getUniqueGiftChatThemes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatThemeUniqueGift  
[Back to constructors index](/API_docs/constructors/index.html)



Set a theme based on an owned [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts), returned by [account.getUniqueGiftChatThemes](../methods/account.getUniqueGiftChatThemes.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|slug|[string](/API_docs/types/string.html) | Yes|The slug from [starGiftUnique](../constructors/starGiftUnique.html).`slug`.|



### Type: [InputChatTheme](/API_docs/types/InputChatTheme.html)


### Example:

```
$inputChatThemeUniqueGift = ['_' => 'inputChatThemeUniqueGift', 'slug' => 'string'];
```  
