from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

import pymysql.cursors
db = pymysql.connect(           
    host="localhost",
    port=8889,
    user="root",
    passwd="root",
    database="ms_product"
)

class ProductModel(BaseModel):
    name: str
    price: float
    stock: int


@app.post('/products')
async def products(product: ProductModel):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = f"INSERT INTO tb_product (name, price, stock) VALUES('{product.name}', '{product.price}', '{product.stock}')"
    res = cursor.execute(sql)
    if res:
        db.commit()
        return {'data': product, 'status': 200}


@app.get('/products')
async def products():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM tb_product"
    cursor.execute(sql)
    res = cursor.fetchall()
    return {'status': 200, 'data': res}