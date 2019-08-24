# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from application import db
# Base = declarative_base()
# metadata = Base.metadata

class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = Column(INTEGER(11), primary_key=True)
    uid = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"), comment='uid')
    referer_url = Column(String(255), nullable=False, server_default=text("''"), comment='当前访问的refer')
    target_url = Column(String(255), nullable=False, server_default=text("''"), comment='访问的url')
    query_params = Column(Text, nullable=False, comment='get和post参数')
    ua = Column(String(255), nullable=False, server_default=text("''"), comment='访问ua')
    ip = Column(String(32), nullable=False, server_default=text("''"), comment='访问ip')
    note = Column(String(1000), nullable=False, server_default=text("''"), comment='json格式备注字段')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
