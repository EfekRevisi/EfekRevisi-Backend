#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class News(object):
    """
    Struct for property criteria parameter.

    Attributes:
     - newsID
     - title
     - thumbnail
     - date
     - description
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'newsID', None, None, ),  # 1
        (2, TType.STRING, 'title', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'thumbnail', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'date', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'description', 'UTF8', None, ),  # 5
    )

    def __init__(self, newsID=None, title=None, thumbnail=None, date=None, description=None,):
        self.newsID = newsID
        self.title = title
        self.thumbnail = thumbnail
        self.date = date
        self.description = description

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.newsID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.thumbnail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.date = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('News')
        if self.newsID is not None:
            oprot.writeFieldBegin('newsID', TType.I64, 1)
            oprot.writeI64(self.newsID)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 2)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.thumbnail is not None:
            oprot.writeFieldBegin('thumbnail', TType.STRING, 3)
            oprot.writeString(self.thumbnail.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnail)
            oprot.writeFieldEnd()
        if self.date is not None:
            oprot.writeFieldBegin('date', TType.STRING, 4)
            oprot.writeString(self.date.encode('utf-8') if sys.version_info[0] == 2 else self.date)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 5)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.newsID is None:
            raise TProtocolException(message='Required field newsID is unset!')
        if self.title is None:
            raise TProtocolException(message='Required field title is unset!')
        if self.thumbnail is None:
            raise TProtocolException(message='Required field thumbnail is unset!')
        if self.date is None:
            raise TProtocolException(message='Required field date is unset!')
        if self.description is None:
            raise TProtocolException(message='Required field description is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class NewsList(object):
    """
    Attributes:
     - items
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'items', (TType.STRUCT, (News, News.thrift_spec), False), None, ),  # 1
    )

    def __init__(self, items=None,):
        self.items = items

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.items = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = News()
                        _elem5.read(iprot)
                        self.items.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('NewsList')
        if self.items is not None:
            oprot.writeFieldBegin('items', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.items))
            for iter6 in self.items:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.items is None:
            raise TProtocolException(message='Required field items is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ErrorHandling(TException):
    """
    Structs can also be exceptions, if they are nasty.

    Attributes:
     - idError
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'idError', None, None, ),  # 1
        (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
    )

    def __init__(self, idError=None, message=None,):
        self.idError = idError
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.idError = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ErrorHandling')
        if self.idError is not None:
            oprot.writeFieldBegin('idError', TType.I32, 1)
            oprot.writeI32(self.idError)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)