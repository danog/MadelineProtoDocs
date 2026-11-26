# payments.validatedRequestedInfo

> Validated user-provided info

[Back to constructors index](/API_docs/constructors/index.html)



Validated user-provided info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Optional|ID|
|shipping\_options|Array of [ShippingOption](/API_docs/types/ShippingOption.html) | Optional|Shipping options|



### Type: [payments.ValidatedRequestedInfo](/API_docs/types/payments.ValidatedRequestedInfo.html)


### Example:

```
$payments_validatedRequestedInfo = ['_' => 'payments.validatedRequestedInfo', 'id' => 'string', 'shipping_options' => [ShippingOption, ShippingOption]];
```
