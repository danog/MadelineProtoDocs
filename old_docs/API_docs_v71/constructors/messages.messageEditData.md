---
title: messages.messageEditData
description: Message edit data for media
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.messageEditData  
[Back to constructors index](index.md)



Message edit data for media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|caption|[Bool](../types/Bool.md) | Optional|Media caption, if the specified media's caption can be edited|



### Type: [messages.MessageEditData](../types/messages.MessageEditData.md)


### Example:

```php
$messages.messageEditData = ['_' => 'messages.messageEditData', 'caption' => Bool];
```  


Or, if you're into Lua:

```lua
messages.messageEditData={_='messages.messageEditData', caption=Bool}

```


