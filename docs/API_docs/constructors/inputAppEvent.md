---
title: "inputAppEvent"
description: "Event that occured in the application."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputAppEvent  
[Back to constructors index](/API_docs/constructors/index.md)



Event that occured in the application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|time|[double](/API_docs/types/double.md) | Yes|Client's exact timestamp for the event|
|type|[string](/API_docs/types/string.md) | Yes|Type of event|
|peer|[long](/API_docs/types/long.md) | Yes|Arbitrary numeric value for more convenient selection of certain event types, or events referring to a certain object|
|data|[JSONValue](/API_docs/types/JSONValue.md) | Yes|Details of the event|



### Type: [InputAppEvent](/API_docs/types/InputAppEvent.md)


### Example:

```php
$inputAppEvent = ['_' => 'inputAppEvent', 'time' => double, 'type' => 'string', 'peer' => long, 'data' => JSONValue];
```  
