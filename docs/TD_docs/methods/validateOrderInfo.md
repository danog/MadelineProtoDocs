---
title: validateOrderInfo
description: Validates order information provided by the user and returns available shipping options for flexible invoice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: validateOrderInfo  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Validates order information provided by the user and returns available shipping options for flexible invoice

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier of the Invoice message | Yes|
|message\_id|[int53](../types/int53.md) | Message identifier | Yes|
|order\_info|[orderInfo](../constructors/orderInfo.md) | Order information, provided by the user | Yes|
|allow\_save|[Bool](../types/Bool.md) | True, if order information can be saved | Yes|


### Return type: [ValidatedOrderInfo](../types/ValidatedOrderInfo.md)

