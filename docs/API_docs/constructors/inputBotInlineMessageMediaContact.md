---
title: "inputBotInlineMessageMediaContact"
description: "A contact"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaContact  
[Back to constructors index](index.md)



A contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|vcard|[string](../types/string.md) | Yes|VCard info|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaContact = ['_' => 'inputBotInlineMessageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaContact={_='inputBotInlineMessageMediaContact', phone_number='string', first_name='string', last_name='string', vcard='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


