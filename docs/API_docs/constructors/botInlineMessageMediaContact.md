---
title: "botInlineMessageMediaContact"
description: "Send a contact"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaContact  
[Back to constructors index](index.md)



Send a contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|vcard|[string](../types/string.md) | Yes|VCard info|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaContact = ['_' => 'botInlineMessageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
botInlineMessageMediaContact={_='botInlineMessageMediaContact', phone_number='string', first_name='string', last_name='string', vcard='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


