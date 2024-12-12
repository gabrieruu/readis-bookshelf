## Notes

1. Ensure that the `instance` directory is writable to create the SQLite database (`books.db`).  
2. Use a tool like Postman, cURL, or any HTTP client to make API requests.  
3. Any info on how to use the api are in the `API_Guide.md` file.

---

## Additional Features

- **Predefined Categories**: Default categories (`Fiction`, `Non-Fiction`, `Sci-Fi`, `Fantasy`) are created for each user.  
- **Authentication**: User sessions are managed with Flask-Login.  

---

## Models and Relationships

### **User**
- Fields: `id`, `name`, `password_hash`, `is_active`
- Relationships:  
  - `books` (One-to-Many with `Book`)  
  - `categories` (One-to-Many with `Category`)

### **Book**
- Fields: `id`, `title`, `author`, `read_list_status`, `buy_list_status`, `user_id`
- Relationships:  
  - `user` (Many-to-One with `User`)  
  - `categories` (Many-to-Many with `Category`)

### **Category**
- Fields: `id`, `name`, `user_id`
- Relationships:  
  - `user` (Many-to-One with `User`)  
  - `books` (Many-to-Many with `Book`)
