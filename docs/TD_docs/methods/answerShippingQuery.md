---
title: answerShippingQuery
description: Bots only. Sets result of a shipping query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: answerShippingQuery  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Sets result of a shipping query

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|shipping\_query\_id|[int64](../constructors/int64.md) | Identifier of the shipping query | Yes|
|shipping\_options|Array of [shippingOption](../constructors/shippingOption.md) | Available shipping options | Yes|
|error\_message|[string](../types/string.md) | Error message, empty on success | Yes|


### Return type: [Ok](../types/Ok.md)

