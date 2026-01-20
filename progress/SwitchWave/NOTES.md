# Recompiled!

Tracking updates for SwitchWave.
Original URL: https://github.com/averne/SwitchWave/
New Url: https://github.com/auggeythecat/SwitchWave/

Started building with docker to more easily make a repoducable build environment.
Dependencies not listed in the readme (see dockerfile)
Has to move away from pgkbuild for libsm2 and libnfs
* libsm2 was simply replaced with a git clone && make install
* libnfs has the process stripped from the pkgbuild file. Now clones, patches, and builds without it. (see dockerfile for more info)
Added `#!/bin/bash` to gimp convert script so it would work in my docker environment.
Had to move `extern "C" u32 __nx_applet_exit_mode, __nx_nv_service_type, __nx_nv_transfermem_size;`, and `extern "C" const char mpv_version[];` out of annoymous namespaces to fix linker errors
