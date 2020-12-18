import sys
import os
from jdlogger import logger
from jd_mask_spider_requests import Jd_Mask_Spider
from QR_Login import JDLogin

if __name__ == '__main__':
    login = JDLogin();
    if login.JD_RQ_login():
        logger.info("登录完成~")
    logger.info("当前进程pid为【%s】", os.getpid())
    a = """
    ==========================
    1.预约商品
    2.秒杀抢购商品
    ==========================
    """
    start_tool = Jd_Mask_Spider()
    logger.info(a)
    if len(sys.argv) > 1:
        gpus = sys.argv[1]
        choice_function = gpus
    else:
        choice_function = input('选择功能:')
    if choice_function == '1':
        start_tool.login()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        start_tool.submit_seckill_order()
    else:
        logger.error('没有此功能')
        sys.exit(1)
