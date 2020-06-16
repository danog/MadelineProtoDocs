---
title: decryptedMessageActionScreenshotMessages
description: A screenshot was taken.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionScreenshotMessages\_8  
[Back to constructors index](index.md)



A screenshot was taken.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|random\_ids|Array of [long](../types/long.md) | Yes|List of affected message ids (that appeared on the screenshot)|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionScreenshotMessages_8 = ['_' => 'decryptedMessageActionScreenshotMessages', 'random_ids' => [long, long]];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionScreenshotMessages_8={_='decryptedMessageActionScreenshotMessages', random_ids={long}}

```


