---
title: "inputDialogPeer"
description: "A peer"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDialogPeer  
[Back to constructors index](index.md)



A peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|



### Type: [InputDialogPeer](../types/InputDialogPeer.md)


### Example:

```php
$inputDialogPeer = ['_' => 'inputDialogPeer', 'peer' => InputPeer];
```  


Or, if you're into Lua:

```lua
inputDialogPeer={_='inputDialogPeer', peer=InputPeer}

```


