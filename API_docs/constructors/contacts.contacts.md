# contacts.contacts

> The current user's contact list and info on users.

[Back to constructors index](/API_docs/constructors/index.html)



The current user's contact list and info on users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|Array of [Contact](/API_docs/types/Contact.html) | Yes|Contact list|
|saved\_count|[int](/API_docs/types/int.html) | Yes|Number of contacts that were saved successfully|
|users|Array of [User](/API_docs/types/User.html) | Yes|User list|



### Type: [contacts.Contacts](/API_docs/types/contacts.Contacts.html)


### Example:

```
$contacts_contacts = ['_' => 'contacts.contacts', 'contacts' => [Contact, Contact], 'saved_count' => int, 'users' => [User, User]];
```
