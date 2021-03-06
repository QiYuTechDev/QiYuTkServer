"""
用户分享淘宝商品
"""

from django.http import HttpRequest

from core.forms import ShareItemTklForm
from core.logger import get_logger
from core.logic import ShareLogic
from core.resp import ShareItemTklResponseModel
from core.resp.base import ApiResp
from ...api.app import app
from ...api_utils import api_inner_wrapper


@app.post(
    "/share/ios/relation_tkl",
    tags=["分享"],
    summary="iOS 使用淘口令分享商品",
    description="用户通过淘口令分享指定的商品\n注意: 这个用户必须绑定渠道ID",
)
async def share_ios_relation_tkl(
    request: HttpRequest, g: ShareItemTklForm
) -> ShareItemTklResponseModel:
    logger = get_logger()

    @api_inner_wrapper(logger)
    async def inner():
        logic = ShareLogic(logger)
        tkl = await logic.share_item(g.item_id, g.token, True)
        logger.bind(tkl=tkl, item_id=g.item_id).info("create tkl")
        return ApiResp.from_data(tkl)

    return await inner


@app.post(
    "/share/ios/no_relation_tkl",
    tags=["分享"],
    summary="iOS 使用淘口令分享商品",
    description="用户通过淘口令分享指定的商品\n注意: 这个用户可以没有绑定渠道ID",
)
async def share_ios_no_relation_tkl(
    request: HttpRequest, g: ShareItemTklForm
) -> ShareItemTklResponseModel:
    logger = get_logger()

    @api_inner_wrapper(logger)
    async def inner():
        logic = ShareLogic(logger)
        tkl = await logic.ios_share_item(g.item_id, g.token, True)
        logger.bind(tkl=tkl, item_id=g.item_id).info("create tkl")
        return ApiResp.from_data(tkl)

    return await inner
