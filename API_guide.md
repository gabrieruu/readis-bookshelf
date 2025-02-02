# API Guide

This guide provides detailed information about the routes available in the API, including their purpose, expected request payloads, and response formats.

---

## Authentication Routes

### **Register a User**
- **Method**: `POST`  
- **Endpoint**: `/register`  
- **Description**: Register a new user.  

**Request Body Example**:  
```json
{
  "name": "JohnDoe",
  "password": "securepassword123"
}
```

**Response Example**:  
```json
{
  "message": "User registered!"
}
```

---

### **Login a User**
- **Method**: `POST`  
- **Endpoint**: `/login`  
- **Description**: Log in an existing user.  

**Request Body Example**:  
```json
{
  "name": "JohnDoe",
  "password": "securepassword123"
}
```

**Response Example**:  
```json
{
  "message": "Logged in successfully!"
}
```

---

### **Logout a User**
- **Method**: `POST`  
- **Endpoint**: `/logout`  
- **Description**: Log out the currently authenticated user.  

**Response Example**:  
```json
{
  "message": "Logged out successfully!"
}
```

---

## Library Management Routes

### **Get All Books**
- **Method**: `GET`  
- **Endpoint**: `/library`  
- **Description**: Retrieve all books in the library.  

**Response Example**:  
```json
[
	{
		"author": "Harper Lee",
		"buy_list_status": "not_owned",
		"read_list_status": "reading",
		"title": "To Kill a Mockingbird"
	}
]
```

---

### **Add a Book**
- **Method**: `POST`  
- **Endpoint**: `/library`  
- **Description**: Add a new book to the library.  

**Request Body Example**:  
```json
{
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "read_list_status": "READING",
  "buy_list_status": "NOT_OWNED"
}
```

**Response Example**:  
```json
{
  "message": "Book added!"
}
```

---

### **Add a Category**
- **Method**: `POST`  
- **Endpoint**: `/categories`  
- **Description**: Add a new book category.  

**Request Body Example**:  
```json
{
  "name": "New Category"
}
```

**Response Example**:  
```json
{
  "message": "Category added!"
}
```

---

## Notes

- **Authorization**: Some routes require user authentication. Ensure your requests include the appropriate authorization token or session information if necessary.
- **Status Codes**: 
  - `200 OK`: Request was successful.  
  - `201 Created`: Resource was successfully created.  
  - `401 Unauthorized`: Authentication is required or failed.  
  - `404 Not Found`: The requested resource does not exist.  
