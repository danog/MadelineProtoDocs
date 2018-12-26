---
title: importedContact
description: Imported contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: importedContact  
[Back to constructors index](index.md)



Imported contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|client\_id|[long](../types/long.md) | Yes|Client ID|



### Type: [ImportedContact](../types/ImportedContact.md)


### Example:

```php
$importedContact = ['_' => 'importedContact', 'user_id' => int, 'client_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "importedContact", "user_id": int, "client_id": long}
```


Or, if you're into Lua:

```lua
importedContact={_='importedContact', user_id=int, client_id=long}

```


