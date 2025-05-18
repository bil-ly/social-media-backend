from fastapi import FastAPI , HTTPException, status,Response
from pydantic import BaseModel
from typing import Dict
import psycopg , time

app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published: bool = True



while True:
    try:
        conn = psycopg.connect("dbname=fastapi_media_app user=postgres password=Abilly#99")
        cursor = conn.cursor()
        print("Success")
        break

    except Exception as error:
        print("Connection failed")
        print(error)
        time.sleep(3)

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return posts


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"The post with id:{id} does not exist")
    return {post}

@app.post("/posts")
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return{new_post}
@app.delete("/posts/{id}")
def delete_post(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id : int,post: Post):
    cursor.execute("""UPDATE posts SET title=%s , content=%s , published=%s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    
    updated_post=cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,detail="post does not exist")
    return {updated_post}
    
