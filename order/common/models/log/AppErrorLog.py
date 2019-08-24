# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from application import db

# Base = declarative_base()
# metadata = Base.metadata


class AppErrorLog(db.Model):
    __tablename__ = 'app_error_log'

    id = Column(INTEGER(11), primary_key=True)
    referer_url = Column(String(255), nullable=False, server_default=text("''"), comment='当前访问的refer')
    target_url = Column(String(255), nullable=False, server_default=text("''"), comment='访问的url')
    query_params = Column(Text, nullable=False, comment='get和post参数')
    content = Column(LONGTEXT, nullable=False, comment='日志内容')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='插入时间')
