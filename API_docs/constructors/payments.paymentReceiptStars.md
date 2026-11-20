# payments.paymentReceiptStars

> Receipt for payment made using Telegram Stars.

[Back to constructors index](/API_docs/constructors/index.html)



Receipt for [payment made using Telegram Stars](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|Date of generation|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|title|[string](/API_docs/types/string.html) | Yes|Title|
|description|[string](/API_docs/types/string.html) | Yes|Description|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Product photo|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|Invoice|
|currency|[string](/API_docs/types/string.html) | Yes|Currency, always `XTR`.|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Amount of [Telegram Stars](https://core.telegram.org/api/stars).|
|transaction\_id|[string](/API_docs/types/string.html) | Yes|Transaction ID|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about users mentioned in the other fields.|



### Type: [payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.html)


### Example:

```
$payments_paymentReceiptStars = ['_' => 'payments.paymentReceiptStars', 'date' => int, 'bot_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'currency' => 'string', 'total_amount' => long, 'transaction_id' => 'string', 'users' => [User, User]];
```
