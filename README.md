# News Publishing Platform

This project is a Django-based **News Publishing Platform** that enables editors to manage news articles through a secure admin interface. Editors can create, update, delete, and publish news articles, each containing a title, content, and a publish date.

The platform features:

- **User Authentication:** Admins can log in and log out securely.
- **Article Management:** Editors can create new articles, edit existing ones, and delete articles via intuitive form-based views.
- **Published Articles Display:** The frontend publicly displays a clean, styled list of all published articles with their titles, publish dates, and content.
- **Role-Based Access:** Only authenticated users (admins/editors) have access to article management features, while all visitors can view published news.
- **Consistent UI:** Shared layout and navigation across pages using Django template inheritance for `base.html`.

---

## Usage

- Navigate to the homepage to view all published articles.
- Log in as an admin/editor to create, edit, or delete articles.
- Use the intuitive forms to manage news content with fields for title, content, and publish date.
- Published articles appear automatically on the public-facing page.
  
---

## Technologies Used

- Python 
- Django Web Framework
- HTML
- CSS

---

## Project Structure Highlights

- `base.html`: Main template layout with navigation and authentication links.
- `published_article.html`: Displays list of published news articles.
- `login.html`: Admin login form.
- `article_form.html`: Form template for creating and editing articles.
- `article_confirm_delete.html`: Confirmation page for article deletion.
- `admin_article_list.html`: Admin view listing all articles with edit/delete options.

---

## Conclusion

This News Publishing Platform provides a solid foundation for managing and displaying news articles in a secure and user-friendly way. It demonstrates key Django features such as authentication, CRUD operations, and template inheritance while maintaining a clean and consistent user interface. 

The project can be easily extended with additional functionality like user roles, article categories, search capabilities, or enhanced styling to better suit production needs. It serves as a practical example for anyone looking to build content management systems or news portals using Django.
