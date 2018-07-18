# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polylinegeom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import vector2d_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='polylinegeom.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x12polylinegeom.proto\x12\x0bgazebo.msgs\x1a\x0evector2d.proto\"@\n\x08Polyline\x12\x0e\n\x06height\x18\x01 \x02(\x01\x12$\n\x05point\x18\x02 \x03(\x0b\x32\x15.gazebo.msgs.Vector2d')
  ,
  dependencies=[vector2d_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POLYLINE = _descriptor.Descriptor(
  name='Polyline',
  full_name='gazebo.msgs.Polyline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='gazebo.msgs.Polyline.height', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='gazebo.msgs.Polyline.point', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=115,
)

_POLYLINE.fields_by_name['point'].message_type = vector2d_pb2._VECTOR2D
DESCRIPTOR.message_types_by_name['Polyline'] = _POLYLINE

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), dict(
  DESCRIPTOR = _POLYLINE,
  __module__ = 'polylinegeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Polyline)
  ))
_sym_db.RegisterMessage(Polyline)


# @@protoc_insertion_point(module_scope)