# *_*coding:utf-8 *_*
import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema

token_field = coreapi.Field(
                name="Authorization",
                required=False,
                location="header",
                schema=coreschema.String(),
                description="格式：JWT 值",
        )
TokenSchema = AutoSchema([
                token_field
        ]
)

GoodTypeSchema = AutoSchema([
    # token_field,
    coreapi.Field(
                "good_id",
                required=False,
                location="query", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="商品ID",
            ),
])

TypeListChema = AutoSchema([
    # token_field,
    coreapi.Field(
                "type_id",
                required=False,
                location="query", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="类型ID",
            ),
])