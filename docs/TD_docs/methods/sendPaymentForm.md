---
title: sendPaymentForm
description: Sends filled payment form to the bot for the final verification
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: sendPaymentForm  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sends filled payment form to the bot for the final verification

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier of the Invoice message | Yes|
|message\_id|[int53](../types/int53.md) | Message identifier | Yes|
|order\_info\_id|[string](../types/string.md) | Identifier returned by ValidateOrderInfo or empty string | Yes|
|shipping\_option\_id|[string](../types/string.md) | Identifier of a chosen shipping option, if applicable | Yes|
|credentials|[InputCredentials](../types/InputCredentials.md) | Credentials choosed by user for payment | Yes|


### Return type: [PaymentResult](../types/PaymentResult.md)

