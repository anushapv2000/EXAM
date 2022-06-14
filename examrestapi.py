from fastapi import FastAPI

app= FastAPI()

prod=[]
buyer=[]
global v
val={}

@app.get("/buyers")
async def listbuy():
    return {"result:": buyer}

@app.get("/products")
async def listprod():
    return {"result:":prod}

@app.post("/buyers")
async def addbuyer(name):
    if name not in buyer:
       buyer.append(name)
       return {"result:":"OK"}
    else:
       return {"result:":"Duplicate entry"}

@app.post("/products")
async def addprod(name):
    if name not in prod:
        prod.append(name)
        return {"result:":"OK"}
    else:
        return {"result":"Duplicate entry"}
count=0

@app.post("/buyers/{buyername}")
async def buy(buyername,prod_name):
    if buyername not in buyer:
        return {"result:":"Error:no buyer {}".format(buyername)}
    else:
        if prod_name not in prod:
            return {"result:":"ERROR: no product {}".format(prod_name)}
        else:
            v={prod_name:count}
            if prod_name not in v:
                v={prod_name:count}
                v[prod_name]=v[prod_name]+1
                val.update(v)
                print("not there",val)
            else:
                v[prod_name]=v[prod_name]+1
                val.update(v)
                print("tehre",val)
            return val
            return {"result:":"OK"}

@app.post("/buyers/{buyername}/purchased")
async def purchase(buyername):
    if buyername in buyer:
        
        return {val}




   
