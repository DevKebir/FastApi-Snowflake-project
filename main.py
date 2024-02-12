from typing import List

from database import ProductTemp, create_connex
from fastapi import FastAPI, HTTPException
from statements import d1, i1, q1, q3, q4, u1

app = FastAPI(
    title = "CUSTOMED SNOWFLAKE API",
    description = "This is a product API for managing snowflake tables."
)

@app.get("/get-data")
def get_all_data():
    """Fetch all data from product table"""
    _,cur = create_connex()
    try:
        result = cur.execute(q1)
        datas = result.fetchmany(size=5)
        total_count = len(datas)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error while fetching data : {e}")
    finally:
        cur.close()
    return {f"data": [data for data in datas], "total": total_count}



@app.get("/get-data/id/{id}")
def get_one_data(id: int):
    """Get one specific data by id from the product table"""
    conn, cur = create_connex()
    try:
        cur.execute(q3, (id,))
        conn.commit()
        data = cur.fetchone()
        if  data is not None:
            return {"ID": id, "Name": data[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error while getting data: {str(e)}")
    finally:
        cur.close()
        conn.close()




@app.post("/add-product", response_model=List[ProductTemp])
def create_product(product: ProductTemp, Id: int):
    """Add a new product to the products table"""
    con, cur = create_connex()
    try:
        #print(i1)
        cur.execute(i1, (product.Id, product.Name, product.Price))
        con.commit()
        # Get the last insertion after  commitment
        cur.execute(q4)
        data = cur.fetchall()
        #print(data)
        if data:
            last_product = data[0]
            product_dict = {
                "Id": last_product[0],
                "Name": last_product[1],
                "Price": last_product[2]
            }
            return [product_dict]
        else:
            raise ValueError("Insertion failed or no data found after insertion.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error while adding data : {str(e)}")
    finally:
        cur.close()
        con.close()
    
    
@app.put("/update-product/{Id}")
def update_product(product: ProductTemp, Id: int):
    """Update a specific product by its ID number"""
    conn, cur = create_connex()
    try:
        cur.execute(u1, (product.Name, product.Price))
        conn.commit()
        cur.execute(q3, (Id,))
        conn.commit()
        d = cur.fetchall()
        print(d)
        ### A completer###
    finally:
        cur.close()
        conn.close()
        

@app.delete("/delete-product/{Id}")
def delete_product(Id : int):
    """Delete a specific product by its ID number"""
    conn, cur = create_connex()
    try:
        cur.execute(d1, (Id,))
    # print(d1, Id)
        conn.commit()
    # Get all products for testing purposes
        cur.execute(q1)
        conn.commit()
        nb_products = cur.fetchall()
        return {f"{len(nb_products)} product left in the database."}
    finally:
        cur.close()
        conn.close()
        
    

    







    





    


