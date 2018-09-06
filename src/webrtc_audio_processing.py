# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_webrtc_audio_processing')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_webrtc_audio_processing')
    _webrtc_audio_processing = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_webrtc_audio_processing', [dirname(__file__)])
        except ImportError:
            import _webrtc_audio_processing
            return _webrtc_audio_processing
        try:
            _mod = imp.load_module('_webrtc_audio_processing', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _webrtc_audio_processing = swig_import_helper()
    del swig_import_helper
else:
    import _webrtc_audio_processing
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class AudioProcessingModule(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AudioProcessingModule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AudioProcessingModule, name)
    __repr__ = _swig_repr

    def __init__(self, aec_type=0, enable_ns=False, agc_type=0, enable_vad=False):
        this = _webrtc_audio_processing.new_AudioProcessingModule(aec_type, enable_ns, agc_type, enable_vad)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def process_stream(self, stream):
        return _webrtc_audio_processing.AudioProcessingModule_process_stream(self, stream)

    def process_reverse_stream(self, data):
        return _webrtc_audio_processing.AudioProcessingModule_process_reverse_stream(self, data)

    def has_echo(self):
        return _webrtc_audio_processing.AudioProcessingModule_has_echo(self)

    def has_voice(self):
        return _webrtc_audio_processing.AudioProcessingModule_has_voice(self)

    def set_system_delay(self, delay):
        return _webrtc_audio_processing.AudioProcessingModule_set_system_delay(self, delay)

    def set_stream_format(self, rate, channels, out_rate=16000, out_channels=1):
        return _webrtc_audio_processing.AudioProcessingModule_set_stream_format(self, rate, channels, out_rate, out_channels)

    def set_reverse_stream_format(self, rate, channels):
        return _webrtc_audio_processing.AudioProcessingModule_set_reverse_stream_format(self, rate, channels)

    def vad_level(self):
        return _webrtc_audio_processing.AudioProcessingModule_vad_level(self)

    def set_vad_level(self, level):
        return _webrtc_audio_processing.AudioProcessingModule_set_vad_level(self, level)

    def ns_level(self):
        return _webrtc_audio_processing.AudioProcessingModule_ns_level(self)

    def set_ns_level(self, level):
        return _webrtc_audio_processing.AudioProcessingModule_set_ns_level(self, level)

    def aec_level(self):
        return _webrtc_audio_processing.AudioProcessingModule_aec_level(self)

    def set_aec_level(self, level):
        return _webrtc_audio_processing.AudioProcessingModule_set_aec_level(self, level)

    def set_agc_level(self, level):
        return _webrtc_audio_processing.AudioProcessingModule_set_agc_level(self, level)

    def agc_level(self):
        return _webrtc_audio_processing.AudioProcessingModule_agc_level(self)
    __swig_destroy__ = _webrtc_audio_processing.delete_AudioProcessingModule
    __del__ = lambda self: None
AudioProcessingModule_swigregister = _webrtc_audio_processing.AudioProcessingModule_swigregister
AudioProcessingModule_swigregister(AudioProcessingModule)

# This file is compatible with both classic and new-style classes.

