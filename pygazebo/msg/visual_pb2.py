# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visual.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pose_pb2
import geometry_pb2
import material_pb2
import plugin_pb2
import vector3d_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='visual.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x0cvisual.proto\x12\x0bgazebo.msgs\x1a\npose.proto\x1a\x0egeometry.proto\x1a\x0ematerial.proto\x1a\x0cplugin.proto\x1a\x0evector3d.proto\"\xcd\x04\n\x06Visual\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x13\n\x0bparent_name\x18\x03 \x02(\t\x12\x11\n\tparent_id\x18\x04 \x01(\r\x12\x14\n\x0c\x63\x61st_shadows\x18\x05 \x01(\x08\x12\x14\n\x0ctransparency\x18\x06 \x01(\x01\x12\x13\n\x0blaser_retro\x18\x07 \x01(\x01\x12\x1f\n\x04pose\x18\x08 \x01(\x0b\x32\x11.gazebo.msgs.Pose\x12\'\n\x08geometry\x18\t \x01(\x0b\x32\x15.gazebo.msgs.Geometry\x12\'\n\x08material\x18\n \x01(\x0b\x32\x15.gazebo.msgs.Material\x12\x0f\n\x07visible\x18\x0b \x01(\x08\x12\x11\n\tdelete_me\x18\x0c \x01(\x08\x12\x11\n\tis_static\x18\r \x01(\x08\x12#\n\x06plugin\x18\x0e \x03(\x0b\x32\x13.gazebo.msgs.Plugin\x12$\n\x05scale\x18\x0f \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12&\n\x04meta\x18\x10 \x01(\x0b\x32\x18.gazebo.msgs.Visual.Meta\x12&\n\x04type\x18\x11 \x01(\x0e\x32\x18.gazebo.msgs.Visual.Type\x1a\x15\n\x04Meta\x12\r\n\x05layer\x18\x01 \x01(\x05\"d\n\x04Type\x12\n\n\x06\x45NTITY\x10\x00\x12\t\n\x05MODEL\x10\x01\x12\x08\n\x04LINK\x10\x02\x12\n\n\x06VISUAL\x10\x03\x12\r\n\tCOLLISION\x10\x04\x12\n\n\x06SENSOR\x10\x05\x12\x07\n\x03GUI\x10\x06\x12\x0b\n\x07PHYSICS\x10\x07')
  ,
  dependencies=[pose_pb2.DESCRIPTOR,geometry_pb2.DESCRIPTOR,material_pb2.DESCRIPTOR,plugin_pb2.DESCRIPTOR,vector3d_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VISUAL_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='gazebo.msgs.Visual.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VISUAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLISION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUI', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICS', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=593,
  serialized_end=693,
)
_sym_db.RegisterEnumDescriptor(_VISUAL_TYPE)


_VISUAL_META = _descriptor.Descriptor(
  name='Meta',
  full_name='gazebo.msgs.Visual.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layer', full_name='gazebo.msgs.Visual.Meta.layer', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=570,
  serialized_end=591,
)

_VISUAL = _descriptor.Descriptor(
  name='Visual',
  full_name='gazebo.msgs.Visual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Visual.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Visual.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_name', full_name='gazebo.msgs.Visual.parent_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='gazebo.msgs.Visual.parent_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cast_shadows', full_name='gazebo.msgs.Visual.cast_shadows', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transparency', full_name='gazebo.msgs.Visual.transparency', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='laser_retro', full_name='gazebo.msgs.Visual.laser_retro', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.Visual.pose', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='gazebo.msgs.Visual.geometry', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material', full_name='gazebo.msgs.Visual.material', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='gazebo.msgs.Visual.visible', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_me', full_name='gazebo.msgs.Visual.delete_me', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_static', full_name='gazebo.msgs.Visual.is_static', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plugin', full_name='gazebo.msgs.Visual.plugin', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='gazebo.msgs.Visual.scale', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meta', full_name='gazebo.msgs.Visual.meta', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Visual.type', index=16,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VISUAL_META, ],
  enum_types=[
    _VISUAL_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=693,
)

_VISUAL_META.containing_type = _VISUAL
_VISUAL.fields_by_name['pose'].message_type = pose_pb2._POSE
_VISUAL.fields_by_name['geometry'].message_type = geometry_pb2._GEOMETRY
_VISUAL.fields_by_name['material'].message_type = material_pb2._MATERIAL
_VISUAL.fields_by_name['plugin'].message_type = plugin_pb2._PLUGIN
_VISUAL.fields_by_name['scale'].message_type = vector3d_pb2._VECTOR3D
_VISUAL.fields_by_name['meta'].message_type = _VISUAL_META
_VISUAL.fields_by_name['type'].enum_type = _VISUAL_TYPE
_VISUAL_TYPE.containing_type = _VISUAL
DESCRIPTOR.message_types_by_name['Visual'] = _VISUAL

Visual = _reflection.GeneratedProtocolMessageType('Visual', (_message.Message,), dict(

  Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(
    DESCRIPTOR = _VISUAL_META,
    __module__ = 'visual_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.Visual.Meta)
    ))
  ,
  DESCRIPTOR = _VISUAL,
  __module__ = 'visual_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Visual)
  ))
_sym_db.RegisterMessage(Visual)
_sym_db.RegisterMessage(Visual.Meta)


# @@protoc_insertion_point(module_scope)
