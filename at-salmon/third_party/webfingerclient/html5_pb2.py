# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_GLOBALATTRIBUTES = descriptor.Descriptor(
  name='GlobalAttributes',
  full_name='GlobalAttributes',
  filename='html5.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ATTRIBUTE = descriptor.Descriptor(
  name='Attribute',
  full_name='Attribute',
  filename='html5.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='Attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_LINK = descriptor.Descriptor(
  name='Link',
  full_name='Link',
  filename='html5.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='global_attributes', full_name='Link.global_attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='custom_attributes', full_name='Link.custom_attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='href', full_name='Link.href', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rel', full_name='Link.rel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='media', full_name='Link.media', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hreflang', full_name='Link.hreflang', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='Link.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sizes', full_name='Link.sizes', index=7,
      number=8, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='Link.title', index=8,
      number=9, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_LINK.fields_by_name['global_attributes'].message_type = _GLOBALATTRIBUTES
_LINK.fields_by_name['custom_attributes'].message_type = _ATTRIBUTE

class GlobalAttributes(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GLOBALATTRIBUTES

class Attribute(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTRIBUTE

class Link(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LINK

