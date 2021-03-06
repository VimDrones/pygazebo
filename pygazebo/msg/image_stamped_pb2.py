# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_stamped.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import time_pb2
import image_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_stamped.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x13image_stamped.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\x1a\x0bimage.proto\"R\n\x0cImageStamped\x12\x1f\n\x04time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12!\n\x05image\x18\x02 \x02(\x0b\x32\x12.gazebo.msgs.Image')
  ,
  dependencies=[time_pb2.DESCRIPTOR,image_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGESTAMPED = _descriptor.Descriptor(
  name='ImageStamped',
  full_name='gazebo.msgs.ImageStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.ImageStamped.time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='gazebo.msgs.ImageStamped.image', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=61,
  serialized_end=143,
)

_IMAGESTAMPED.fields_by_name['time'].message_type = time_pb2._TIME
_IMAGESTAMPED.fields_by_name['image'].message_type = image_pb2._IMAGE
DESCRIPTOR.message_types_by_name['ImageStamped'] = _IMAGESTAMPED

ImageStamped = _reflection.GeneratedProtocolMessageType('ImageStamped', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESTAMPED,
  __module__ = 'image_stamped_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.ImageStamped)
  ))
_sym_db.RegisterMessage(ImageStamped)


# @@protoc_insertion_point(module_scope)
