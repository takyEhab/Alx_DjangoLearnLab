# Bookshelf App - Permissions and Groups Setup

## Custom Permissions
The `Book` model has the following permissions:
- `can_view` - Allows viewing books
- `can_create` - Allows adding new books
- `can_edit` - Allows editing books
- `can_delete` - Allows deleting books

## Groups and Permissions
| Group   | can_view | can_create | can_edit | can_delete |
|---------|---------|------------|---------|------------|
| Viewers | ✅       | ❌        | ❌       | ❌        |
| Editors | ✅       | ✅        | ✅       | ❌        |
| Admins  | ✅       | ✅        | ✅       | ✅        |

## Applying Permissions in Views
Views use `@permission_required()` to restrict access:
- `book_list` → Requires `can_view`
- `book_create` → Requires `can_create`
- `book_edit` → Requires `can_edit`
- `book_delete` → Requires `can_delete`

## Testing
1. **Create test users** and assign them to groups.
2. **Log in as different users** and verify what actions they can/cannot perform.
3. **Try unauthorized actions** to confirm Django blocks them.

## Additional Notes
- Manage groups and users in Django Admin under **Authentication and Authorization**.
- You can customize groups and permissions as needed.
