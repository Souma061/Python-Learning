from typing import List, Optional
from pydantic import BaseModel



class Comment(BaseModel):
    id:int
    content:str
    replies: Optional[List['Comment']] = None  # Self-referential field for nested comments


Comment.model_rebuild()  # Rebuild the model to resolve self-references.this is necessary when using self-referential models. If I not call model_rebuild(), Pydantic will not be able to resolve the self-references and will raise an error when trying to create instances of the Comment model and there will be ahuge performance impact when creating instances of the Comment model, as Pydantic will have to resolve the self-references every time an instance is created. By calling model_rebuild(), Pydantic will resolve the self-references once and cache the results, improving performance when creating instances of the Comment model.

comment_1 = Comment(
    id=1,
    content="This is the first comment.",
    replies=[
        Comment(
            id=2,
            content="This is a reply to the first comment.",
            replies=[
                Comment(
                    id=3,
                    content="This is a nested reply to the first comment."
                )
            ]
        )
    ]
)

print(f"Comment ID: {comment_1.id}, Content: {comment_1.content}")
if comment_1.replies:
    for reply in comment_1.replies:
        print(f"  Reply ID: {reply.id}, Content: {reply.content}")
        if reply.replies:
            for nested_reply in reply.replies:
                print(f"    Nested Reply ID: {nested_reply.id}, Content: {nested_reply.content}")
