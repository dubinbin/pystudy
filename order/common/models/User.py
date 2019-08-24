# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# metadata = Base.metadata

from application import db

class User(db.Model):
    __tablename__ = 'user'

    uid = Column(BIGINT(20), primary_key=True, comment='用户uid')
    nickname = Column(String(100), nullable=False, server_default=text("''"), comment='用户名')
    mobile = Column(String(20), nullable=False, server_default=text("''"), comment='手机号码')
    email = Column(String(100), nullable=False, server_default=text("''"), comment='邮箱地址')
    sex = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='1：男 2：女 0：没填写')
    avatar = Column(String(64), nullable=False, server_default=text("''"), comment='头像')
    login_name = Column(String(20), nullable=False, unique=True, server_default=text("''"), comment='登录用户名')
    login_pwd = Column(String(32), nullable=False, server_default=text("''"), comment='登录密码')
    login_salt = Column(String(32), nullable=False, server_default=text("''"), comment='登录密码的随机加密秘钥')
    status = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='1：有效 0：无效')
    updated_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='最后一次更新时间')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='插入时间')
