# inputStorePaymentPremiumSubscription

> Info about a Telegram Premium purchase

[Back to constructors index](/API_docs/constructors/index.html)



Info about a Telegram Premium purchase

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|restore|[Bool](/API_docs/types/Bool.html) | Optional|Pass true if this is a restore of a Telegram Premium purchase; only for the App Store|
|upgrade|[Bool](/API_docs/types/Bool.html) | Optional|Pass true if this is an upgrade from a monthly subscription to a yearly subscription; only for App Store|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumSubscription = ['_' => 'inputStorePaymentPremiumSubscription', 'restore' => Bool, 'upgrade' => Bool];
```
