# contacts.contactBirthdays

> Birthday information of our contacts.

[Back to constructors index](/API_docs/constructors/index.html)



Birthday information of our contacts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [ContactBirthday](/API_docs/types/ContactBirthday.html) | Yes|Birthday info|
|users|Array of [User](/API_docs/types/User.html) | Yes|User information|



### Type: [contacts.ContactBirthdays](/API_docs/types/contacts.ContactBirthdays.html)


### Example:

```
$contacts_contactBirthdays = ['_' => 'contacts.contactBirthdays', 'contacts' => [ContactBirthday, ContactBirthday], 'users' => [User, User]];
```
