---
title: "botInlineMessageMediaContact"
description: "Send a contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaContact  
[Back to constructors index](/API_docs/constructors/index.html)



Send a contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.html) | Yes|First name|
|last\_name|[string](/API_docs/types/string.html) | Yes|Last name|
|vcard|[string](/API_docs/types/string.html) | Yes|VCard info|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$botInlineMessageMediaContact = ['_' => 'botInlineMessageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string', 'reply_markup' => ReplyMarkup];
```  
