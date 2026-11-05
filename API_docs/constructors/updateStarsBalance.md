# updateStarsBalance

> The current account's Telegram Stars balance » has changed.

[Back to constructors index](/API_docs/constructors/index.html)



The current account's [Telegram Stars balance »](https://core.telegram.org/api/stars) has changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|New balance.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStarsBalance = ['_' => 'updateStarsBalance', 'balance' => StarsAmount];
```
