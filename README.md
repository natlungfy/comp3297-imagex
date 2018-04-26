# imagex
Repo for imageX project

## Prerequisites (Please install the following in your environment via pip install):
1. Django
2. Pillow
3. django-allauth
4. django_invitations

## Remarks:
* The database has been prepopulated with Categories. Errors will occur if it is flushed/cleared. 
* Clicking the "Like" button increases like count and redirects to the profile of that image's photographer.
* Admin panel is accessible at localhost:8000/admin
* There are 3 accounts available for testing. Of course, you can invite new members and register new accounts / create new superusers.
| Level           | Username | Password  |
|-----------------|----------|-----------|
| Superuser/Admin | nexus    | nexus3297 |
| Member          | nat      | 12345678! |
| Member          | shutsch  | 12345678! |