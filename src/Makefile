

SWIG := swig

WEBRTCLIBFILE = ../webrtc-audio-processing/webrtc/modules/audio_processing/.libs/libwebrtc_audio_processing.a

# PY_CONFIG := $(shell python-config --cflags)
PY_CONFIG := -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE

CXXFLAGS :=  -fPIC -std=c++11 -I. -I../webrtc-audio-processing  $(PY_CONFIG) -DWEBRTC_AUDIO_PROCESSING_ONLY_BUILD -DWEBRTC_LINUX -DWEBRTC_POSIX -DWEBRTC_NS_FLOAT
LDFLAGS := -shared $(shell python-config --ldflags) -lpthread
CXX := g++


all: _webrtc_audio_processing.so _audio_processing_module.so

webrtc_audio_processing_wrap.cpp: webrtc_audio_processing.i
	$(SWIG) -I. -c++ -python -o $@ $^

_webrtc_audio_processing.so: webrtc_audio_processing_wrap.o audio_processing_module.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^ $(WEBRTCLIBFILE)

audio_processing_module_swig.cpp: audio_processing_module.i
	$(SWIG) -I. -c++ -python -o $@ $^

_audio_processing_module.so: audio_processing_module_swig.o audio_processing_module.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^ $(WEBRTCLIBFILE)

clean:
	-rm -f webrtc_audio_processing_wrap.cpp *.o _webrtc_audio_processing.so webrtc_audio_processing.py *.pyc audio_processing_module_swig.cc *.o _audio_processing_module.so audio_processing_module.py *.pyc
