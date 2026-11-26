# payments.starGiftOnchainOfferTxMessage

> payments.starGiftOnchainOfferTxMessage attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|destination|[string](/API_docs/types/string.html) | Yes|
|value|[long](/API_docs/types/long.html) | Yes|
|mode|[int](/API_docs/types/int.html) | Yes|
|body|[bytes](/API_docs/types/bytes.html) | Yes|
|init\_state|[payments.StarGiftOnchainOfferTxInitState](/API_docs/constructors/payments.StarGiftOnchainOfferTxInitState.html) | Optional|



### Type: [payments.StarGiftOnchainOfferTxMessage](/API_docs/types/payments.StarGiftOnchainOfferTxMessage.html)


### Example:

```
$payments_starGiftOnchainOfferTxMessage = ['_' => 'payments.starGiftOnchainOfferTxMessage', 'destination' => 'string', 'value' => long, 'mode' => int, 'body' => 'bytes', 'init_state' => payments.StarGiftOnchainOfferTxInitState];
```
