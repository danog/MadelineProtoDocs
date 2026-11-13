# inputInvoiceStars

> Used to top up the Telegram Stars balance of the current account or someone else's account, or to start a Telegram Star giveaway ».

[Back to constructors index](/API_docs/constructors/index.html)



Used to top up the [Telegram Stars](https://core.telegram.org/api/stars) balance of the current account or someone else's account, or to start a [Telegram Star giveaway »](https://core.telegram.org/api/giveaways#star-giveaways).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Yes|An [inputStorePaymentStarsGiveaway](../constructors/inputStorePaymentStarsGiveaway.html), [inputStorePaymentStarsTopup](../constructors/inputStorePaymentStarsTopup.html) or [inputStorePaymentStarsGift](../constructors/inputStorePaymentStarsGift.html).|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStars = ['_' => 'inputInvoiceStars', 'purpose' => InputStorePaymentPurpose];
```
