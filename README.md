# API
## Clone project
```sh
$ git clone https://github.com/emeraldlynx/kvartirka-django.git
```

## Build and run
### **Docker**
Start docker
```sh
$ sudo dockerd
```
Build and run app
```sh
$ docker-compose up
```

***Also you can manually install all dependencies with `reqiurements.txt` or `Pipfile` files***

---

## API routes

Functionality

- [View articles list](#post-list-get)<br>
- [Adding an article](#post-list-post)<br>
- [View post info](#post-get)<br>
- [View post comments tree](#comment-list-get)<br>
- [Adding a comment to the article](#comment-list-post)<br>
- [View the tree of replies to an article's comment ](#comment-get)<br>

Routes

> `/api/posts` [<span style=color:#00D4FF>GET</span>] [<span style=color:#2EFF00>POST</span>]<br>
> `/api/post/{id}` [<span style=color:#00D4FF>GET</span>]<br>
> `/api/post/{id}/comments` [<span style=color:#00D4FF>GET</span>] [<span style=color:#2EFF00>POST</span>]<br>
> `/api/post/{id}/comment/{id}` [<span style=color:#00D4FF>GET</span>]<br>

## Posts (articles)

<a id="post-list-get" name="post-list-get">#</a> **View articles list** [<span style=color:#00D4FF>GET</span>]

### Route: `/api/posts`<br><br>

response:<br>
```json
{
    "posts": [
        {
            "id": 1,
            "title": "Post 1",
            "text": "Text...",
            "author": "User1"
        },
        {
            "id": 2,
        ...
        }
    ...
}
```

<a id="post-list-post" name="post-list-post">#</a> **Adding an article** [<span style=color:#2EFF00>POST</span>]<br>

### Route: `/api/posts`<br><br>

request:<br>
```json
{
    "post": {
        "title": "Post 3",
        "text": "Text...",
        "author": "User5" 
    }
}
```
response:<br>
```json
{
    "success": "Post '{'title': 'Post 3', 'text': 'Text...', 'author': 'User5'}' created successfully"
}
```

<a id="post-get" name="post-get">#</a> **View post info** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/post/1/{id}`<br><br>

response:<br>
```json
{
    "post": {
        "id": 1,
        "title": "Post 1",
        "text": "Text...",
        "author": "User1"
    }
}
```

## Comments

<a id="comment-list-get" name="comment-list-get">#</a> **View post comments tree** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/post/{id}/comments`<br><br>

You can configure the maximum level of the tree by setting the `nesting-level` parameter in the URL<br>
Default value is `99`.<br>
*Example: `/api/post/3/comments/?nesting-level=1`*

response:<br>
```json
{
    "comments": [
        {
            "id": 1,
            "post": 1,
            "parent": null,
            "author": "Comment 1",
            "text": "Comment 1",
            "replies": [
                {
                    "id": 2,
                    "post": 1,
                    "parent": 1,
                    "author": "User3",
                    "text": "Reply 1",
                    "replies": []
                }
            ]
        },
        {
            "id": 3,
            "post": 1,
            "parent": null,
            "author": "Comment 2",
            "text": "Comment 2",
            "replies": []
        },
        {
            "id": 4,
            "post": 1,
            "parent": null,
            "author": "Comment 3",
            "text": "Comment 3",
            "replies": [
                {
                    "id": 5,
                    "post": 1,
                    "parent": 4,
                    "author": "Reply 2",
                    "text": "Reply 2",
                    "replies": [
                        {
                            "id": 6,
                            "post": 1,
                            "parent": 5,
                            "author": "Reply 2 1",
                            "text": "Reply 2 1",
                            "replies": null
                        },
                        {
                            "id": 7,
                            "post": 1,
                            "parent": 5,
                            "author": "Reply 2 2",
                            "text": "Reply 2 2",
                            "replies": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

<a id="comment-list-post" name="comment-list-post">#</a>  **Adding a comment to the article** [<span style=color:#2EFF00>POST</span>]<br>

### Route: `/api/post/{id}/comments`<br><br>

`parent` can be `null` if object is a comment, or an integer value equal to related object `id` if reply <br>

request:<br>
```json
{
    "parent": null,
    "author": "User28",
    "text": "Text..."
}
```

response:<br>
```json
{
    "success": "Comment '{'post': '3', 'parent': None, 'author': 'User28', 'text': 'Text...'}' created successfully"
}
```

<a id="comment-get" name="comment-get">#</a> **View the tree of replies to an article's comment** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/post/{id}/comment/{id}`<br><br>

You can configure the maximum level of the tree by setting the `nesting-level` parameter in the URL<br>
If you want to get comment info without tree set `nesting-level=1` in URL<br>
Default value is `3`.<br>
*Example: `/api/post/3/comment/4/?nesting-level=1`*<br>

response:<br>
```json
{
    "comment": [
        {
            "id": 4,
            "post": 1,
            "parent": null,
            "author": "Comment 3",
            "text": "Comment 3",
            "replies": [
                {
                    "id": 5,
                    "post": 1,
                    "parent": 4,
                    "author": "Reply 2",
                    "text": "Reply 2",
                    "replies": [
                        {
                            "id": 6,
                            "post": 1,
                            "parent": 5,
                            "author": "Reply 2 1",
                            "text": "Reply 2 1",
                            "replies": null
                        },
                        {
                            "id": 7,
                            "post": 1,
                            "parent": 5,
                            "author": "Reply 2 2",
                            "text": "Reply 2 2",
                            "replies": null
                        }
                    ]
                }
            ]
        }
    ]
}
```
