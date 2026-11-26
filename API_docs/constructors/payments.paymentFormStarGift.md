# payments.paymentFormStarGift

> Represents a payment form for a gift, see here » for more info.

[Back to constructors index](/API_docs/constructors/index.html)



Represents a payment form for a [gift, see here »](https://core.telegram.org/api/gifts) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|form\_id|[long](/API_docs/types/long.html) | Yes|Form ID.|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|Invoice|



### Type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)


### Example:

```
$payments_paymentFormStarGift = ['_' => 'payments.paymentFormStarGift', 'form_id' => long, 'invoice' => Invoice];
```
