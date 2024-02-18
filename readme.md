### Snowflake FastAPI Project

This project implements a FastAPI-based RESTful API for managing products in a Snowflake database. It provides endpoints for fetching, adding, updating, and deleting product data.

### Features

- **Fetch Data**: Retrieve all product data from the Snowflake database.
- **Get Single Data**: Retrieve a specific product by its ID or Name.
- **Add Product**: Add a new product to the database.
- **Update Product**: Update an existing product.
- **Delete Product**: Delete a product from the database.

### Requirements

To run this project, you need:

- Python 3.x
- Snowflake Connector for Python
- FastAPI and uvicorn

### Installation

1. Clone this repository:

   ```bash
   git clone <https://github.com/abkebir/FastApi-Snowflake-project.git>
   
2. Navigate to the project directory:

   ````bash
   cd FastApi-Snowflake-project

3. Create a virtual environment (optional but recommended):

   `bash python -m venv env`

4. Activate your virtual environment (if you created one):

   Windows:
   `cmd env\Scripts\activate`

   Unix or MacOS:
   `source env/bin/activate`

5. Install dependencies with pip:

   bash `pip install fastapi[all] uvicorn snowflake-connector-python

### Usage
1. Launch  Uvicorn server :
bash `uvicorn main:app --host=127.0.0.1 --port=8000`

2. Open your browser and go to http://localhost:8000/docs

### Notes
- Ensure your Snowflake credentials are correctly configured for database access.
- Error handling is implemented to provide meaningful error messages when operations fail.

        
   

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests. Happy coding!


