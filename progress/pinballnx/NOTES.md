# None

Tracking updates for pinballnx.
Original URL: https://github.com/minkcv/pinballnx/releases

Created dockerfile for a more consistant build environment:
```
> docker build -t pinball
+] Building 21.0s (8/8) FINISHED                                                                                                                                           docker:desktop-linux
 => [internal] load build definition from dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 672B                                                                                                                                                        0.0s 
 => [internal] load metadata for docker.io/devkitpro/devkita64:latest                                                                                                                       0.0s 
 => [internal] load .dockerignore                                                                                                                                                           0.0s 
 => => transferring context: 2B                                                                                                                                                             0.0s 
 => [1/5] FROM docker.io/devkitpro/devkita64:latest                                                                                                                                         0.0s 
 => CACHED [2/5] RUN dkp-pacman -Syu --noconfirm      switch-dev      switch-bzip2      switch-freetype      switch-glad      switch-glm      switch-libdrm_nouveau      switch-libpng      0.0s 
 => [3/5] RUN git clone --recurse-submodules https://github.com/minkcv/pinballnx.git                                                                                                        5.0s 
 => [4/5] WORKDIR /pinballnx                                                                                                                                                                0.2s
 => ERROR [5/5] RUN mkdir cmake-build && cd cmake-build &&     cmake -DPLATFORM_SWITCH=ON -DCMAKE_BUILD_TYPE=Release ../ &&     make pinball.nro -j$(nproc)                                15.5s
------
 > [5/5] RUN mkdir cmake-build && cd cmake-build &&     cmake -DPLATFORM_SWITCH=ON -DCMAKE_BUILD_TYPE=Release ../ &&     make pinball.nro -j$(nproc):
0.418 CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
0.418   Compatibility with CMake < 3.10 will be removed from a future version of
0.418   CMake.
0.418 
0.418   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
0.418   to tell CMake that the project requires at least <min> but has been updated
0.418   to work with policies introduced by <max> or earlier.
0.418
0.418
0.420 CMake Deprecation Warning at libcross2d/CMakeLists.txt:1 (cmake_minimum_required):
0.420   Compatibility with CMake < 3.10 will be removed from a future version of
0.420   CMake.
0.420
0.420   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
0.420   to tell CMake that the project requires at least <min> but has been updated
0.420   to work with policies introduced by <max> or earlier.
0.420
0.420
0.420 -- C2D: SDL2 OpenGL 3.3 support enabled
0.422 -- C2D: target platform: switch, cmake version: 3.31.6
0.500 -- The C compiler identification is GNU 15.2.0
0.560 -- The CXX compiler identification is GNU 15.2.0
0.578 -- Detecting C compiler ABI info
0.686 -- Detecting C compiler ABI info - done
0.696 -- Check for working C compiler: /opt/devkitpro/devkitA64/bin/aarch64-none-elf-gcc - skipped
0.697 -- Detecting C compile features
0.697 -- Detecting C compile features - done
0.702 -- Detecting CXX compiler ABI info
0.795 -- Detecting CXX compiler ABI info - done
0.805 -- Check for working CXX compiler: /opt/devkitpro/devkitA64/bin/aarch64-none-elf-g++ - skipped
0.806 -- Detecting CXX compile features
0.806 -- Detecting CXX compile features - done
0.819 -- Found PkgConfig: /usr/bin/pkg-config (found version "1.8.1")
0.820 -- Checking for one of the modules 'zlib'
0.862 -- Checking for one of the modules 'freetype2'
0.906 -- Checking for one of the modules 'sdl2'
0.953 CMake Deprecation Warning at libcross2d/cmake/targets.cmake:1 (cmake_minimum_required):
0.953   Compatibility with CMake < 3.10 will be removed from a future version of
0.953   CMake.
0.953
0.953   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
0.953   to tell CMake that the project requires at least <min> but has been updated
0.953   to work with policies introduced by <max> or earlier.
0.953 Call Stack (most recent call first):
0.953   libcross2d/CMakeLists.txt:305 (include)
0.953
0.953
0.967 CMake Deprecation Warning at games/pinball/CMakeLists.txt:1 (cmake_minimum_required):
0.967   Compatibility with CMake < 3.10 will be removed from a future version of
0.967   CMake.
0.967
0.967   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
0.967   to tell CMake that the project requires at least <min> but has been updated
0.967   to work with policies introduced by <max> or earlier.
0.967
0.967
0.967 CMake Deprecation Warning at libcross2d/cmake/targets.cmake:1 (cmake_minimum_required):
0.967   Compatibility with CMake < 3.10 will be removed from a future version of
0.967   CMake.
0.967
0.967   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
0.967   to tell CMake that the project requires at least <min> but has been updated
0.967   to work with policies introduced by <max> or earlier.
0.967 Call Stack (most recent call first):
0.967   games/pinball/CMakeLists.txt:35 (include)
0.967
0.967
0.968 -- Configuring done (0.6s)
1.006 -- Generating done (0.0s)
1.007 -- Build files have been written to: /pinballnx/cmake-build
1.082 [  1%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/audio.cpp.obj
1.082 [  1%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/config.cpp.obj
1.082 [  1%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/config_option.cpp.obj
1.084 [  2%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/input.cpp.obj
1.084 [  3%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/object.cpp.obj
1.084 [  4%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Clock.cpp.obj
1.084 [  6%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/font.cpp.obj
1.084 [  6%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/CircleShape.cpp.obj
1.084 [  7%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Color.cpp.obj
1.084 [  7%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/renderer.cpp.obj
1.085 [  7%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/ConvexShape.cpp.obj
1.086 [  8%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/Shapes/b2CircleShape.cpp.obj
1.088 [  8%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/Shapes/b2ChainShape.cpp.obj
1.091 [  9%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/config_group.cpp.obj
1.094 [ 10%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/Shapes/b2EdgeShape.cpp.obj
1.121 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.121   Compatibility with CMake < 3.10 will be removed from a future version of
1.121   CMake.
1.121
1.121   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.121   to tell CMake that the project requires at least <min> but has been updated
1.121   to work with policies introduced by <max> or earlier.
1.121
1.121
1.184 [ 10%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/Shapes/b2PolygonShape.cpp.obj
1.189 [ 11%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2BroadPhase.cpp.obj
1.212 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.212   Compatibility with CMake < 3.10 will be removed from a future version of
1.212   CMake.
1.212
1.212   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.212   to tell CMake that the project requires at least <min> but has been updated
1.212   to work with policies introduced by <max> or earlier.
1.212
1.212
1.235 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.235   Compatibility with CMake < 3.10 will be removed from a future version of
1.235   CMake.
1.235
1.235   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.235   to tell CMake that the project requires at least <min> but has been updated
1.235   to work with policies introduced by <max> or earlier.
1.235
1.235
1.271 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.271   Compatibility with CMake < 3.10 will be removed from a future version of
1.271   CMake.
1.271
1.271   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.271   to tell CMake that the project requires at least <min> but has been updated
1.271   to work with policies introduced by <max> or earlier.
1.271
1.271
1.307 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.307   Compatibility with CMake < 3.10 will be removed from a future version of
1.307   CMake.
1.307
1.307   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.307   to tell CMake that the project requires at least <min> but has been updated
1.307   to work with policies introduced by <max> or earlier.
1.307
1.307
1.389 /pinballnx/Box2D/Collision/Shapes/b2ChainShape.cpp: In member function 'void b2ChainShape::CreateLoop(const b2Vec2*, int32)':
1.389 /pinballnx/Box2D/Collision/Shapes/b2ChainShape.cpp:47:24: warning: variable 'v1' set but not used [-Wunused-but-set-variable]
1.389    47 |                 b2Vec2 v1 = vertices[i-1];
1.389       |                        ^~
1.389 /pinballnx/Box2D/Collision/Shapes/b2ChainShape.cpp:48:24: warning: variable 'v2' set but not used [-Wunused-but-set-variable]
1.389    48 |                 b2Vec2 v2 = vertices[i];
1.389       |                        ^~
1.441 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.441   Compatibility with CMake < 3.10 will be removed from a future version of
1.441   CMake.
1.441
1.441   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.441   to tell CMake that the project requires at least <min> but has been updated
1.441   to work with policies introduced by <max> or earlier.
1.441
1.441
1.466 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.466   Compatibility with CMake < 3.10 will be removed from a future version of
1.466   CMake.
1.466
1.466   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.466   to tell CMake that the project requires at least <min> but has been updated
1.466   to work with policies introduced by <max> or earlier.
1.466
1.466
1.469 [ 12%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Font.cpp.obj
1.489 CMake Deprecation Warning at /pinballnx/libcross2d/cmake/copy_directory_custom.cmake:1 (cmake_minimum_required):
1.489   Compatibility with CMake < 3.10 will be removed from a future version of
1.489   CMake.
1.489
1.489   Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
1.489   to tell CMake that the project requires at least <min> but has been updated
1.489   to work with policies introduced by <max> or earlier.
1.489
1.490
1.514 [ 12%] Built target pinball.data
1.542 [ 13%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2CollideCircle.cpp.obj
1.566 [ 14%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Rectangle.cpp.obj
1.570 [ 14%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/RectangleShape.cpp.obj
1.593 [ 15%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/RoundedRectangleShape.cpp.obj
1.699 [ 16%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Shape.cpp.obj
1.974 [ 17%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2CollideEdge.cpp.obj
2.013 [ 18%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Sprite.cpp.obj
2.042 [ 18%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2CollidePolygon.cpp.obj
2.157 [ 18%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Text.cpp.obj
2.196 [ 19%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Time.cpp.obj
2.385 [ 20%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2Collision.cpp.obj
2.481 [ 21%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2Distance.cpp.obj
2.482 [ 22%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Transform.cpp.obj
2.495 [ 23%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Transformable.cpp.obj
2.536 [ 23%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/Vertex.cpp.obj
2.616 [ 23%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2DynamicTree.cpp.obj
2.661 [ 24%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/sfml/VertexArray.cpp.obj
2.862 /pinballnx/Box2D/Collision/b2DynamicTree.cpp: In constructor 'b2DynamicTree::b2DynamicTree()':
2.862 /pinballnx/Box2D/Collision/b2DynamicTree.cpp:29:15: warning: 'void* memset(void*, int, size_t)' clearing an object of non-trivial type 'struct b2TreeNode'; use assignment or value-initialization instead [-Wclass-memaccess]
2.862    29 |         memset(m_nodes, 0, m_nodeCapacity * sizeof(b2TreeNode));
2.862       |         ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.863 In file included from /pinballnx/Box2D/Collision/b2DynamicTree.cpp:19:
2.863 /pinballnx/Box2D/include/Box2D/Collision/b2DynamicTree.h:28:8: note: 'struct b2TreeNode' declared here
2.863    28 | struct b2TreeNode
2.863       |        ^~~~~~~~~~
2.876 /pinballnx/Box2D/Collision/b2DynamicTree.cpp: In member function 'void b2DynamicTree::ValidateMetrics(int32) const':
2.876 /pinballnx/Box2D/Collision/b2DynamicTree.cpp:639:15: warning: variable 'height' set but not used [-Wunused-but-set-variable]
2.876   639 |         int32 height;
2.876       |               ^~~~~~
2.955 [ 25%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/texture.cpp.obj
3.209 [ 25%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/tween.cpp.obj
3.259 In file included from /pinballnx/Box2D/include/Box2D/Collision/b2Distance.h:23,
3.259                  from /pinballnx/Box2D/Collision/b2Distance.cpp:19:
3.259 In function 'b2Vec2 operator+(const b2Vec2&, const b2Vec2&)',
3.259     inlined from 'bool b2ShapeCast(b2ShapeCastOutput*, const b2ShapeCastInput*)' at /pinballnx/Box2D/Collision/b2Distance.cpp:732:40:
3.259 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:430:43: warning: 'pointA.b2Vec2::x' may be used uninitialized [-Wmaybe-uninitialized]
3.259   430 |         return b2Vec2(a.x + b.x, a.y + b.y);
3.259       |                                           ^
3.259 /pinballnx/Box2D/Collision/b2Distance.cpp: In function 'bool b2ShapeCast(b2ShapeCastOutput*, const b2ShapeCastInput*)':
3.259 /pinballnx/Box2D/Collision/b2Distance.cpp:723:16: note: 'pointA.b2Vec2::x' was declared here
3.259   723 |         b2Vec2 pointA, pointB;
3.259       |                ^~~~~~
3.259 In function 'b2Vec2 operator+(const b2Vec2&, const b2Vec2&)',
3.259     inlined from 'bool b2ShapeCast(b2ShapeCastOutput*, const b2ShapeCastInput*)' at /pinballnx/Box2D/Collision/b2Distance.cpp:732:40:
3.259 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:430:43: warning: 'pointA.b2Vec2::y' may be used uninitialized [-Wmaybe-uninitialized]
3.259   430 |         return b2Vec2(a.x + b.x, a.y + b.y);
3.259       |                                           ^
3.260 /pinballnx/Box2D/Collision/b2Distance.cpp: In function 'bool b2ShapeCast(b2ShapeCastOutput*, const b2ShapeCastInput*)':
3.260 /pinballnx/Box2D/Collision/b2Distance.cpp:723:16: note: 'pointA.b2Vec2::y' was declared here
3.260   723 |         b2Vec2 pointA, pointB;
3.260       |                ^~~~~~
3.287 [ 26%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/skeleton/utility.cpp.obj
3.346 [ 27%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/button.cpp.obj
3.566 [ 28%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Collision/b2TimeOfImpact.cpp.obj
3.582 [ 29%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2BlockAllocator.cpp.obj
3.728 [ 30%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/configbox.cpp.obj
3.736 [ 31%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2Draw.cpp.obj
3.900 [ 31%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/listbox.cpp.obj
4.076 [ 32%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/messagebox.cpp.obj
4.268 [ 32%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2Math.cpp.obj
4.290 [ 33%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2Settings.cpp.obj
4.299 [ 34%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/progress.cpp.obj
4.311 [ 35%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2StackAllocator.cpp.obj
4.393 [ 36%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Common/b2Timer.cpp.obj
4.455 [ 36%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/widgets/textbox.cpp.obj
4.601 [ 37%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/sdl2/sdl2_audio.cpp.obj
4.684 [ 37%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2ChainAndCircleContact.cpp.obj
4.777 [ 38%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2ChainAndPolygonContact.cpp.obj
4.906 [ 39%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2CircleContact.cpp.obj
5.177 [ 39%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2Contact.cpp.obj
5.240 [ 40%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2ContactSolver.cpp.obj
5.376 [ 41%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2EdgeAndCircleContact.cpp.obj
5.415 [ 42%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/sdl2/sdl2_gl_renderer.cpp.obj
5.434 [ 43%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2EdgeAndPolygonContact.cpp.obj
5.493 [ 43%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2PolygonAndCircleContact.cpp.obj
5.510 [ 44%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/sdl2/sdl2_input.cpp.obj
5.692 [ 45%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Contacts/b2PolygonContact.cpp.obj
5.733 [ 46%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2DistanceJoint.cpp.obj
5.970 [ 47%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2FrictionJoint.cpp.obj
5.986 [ 47%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/sdl2/sdl2_renderer.cpp.obj
5.992 [ 47%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2GearJoint.cpp.obj
6.004 [ 48%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2Joint.cpp.obj
6.039 [ 50%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2MotorJoint.cpp.obj
6.049 [ 51%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/sdl2/sdl2_texture.cpp.obj
6.074 [ 52%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/gl_renderer.cpp.obj
6.109 [ 53%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/gl_shaders.cpp.obj
6.165 [ 53%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2MouseJoint.cpp.obj
6.209 In file included from /pinballnx/Box2D/include/Box2D/Dynamics/Contacts/b2ContactSolver.h:22,
6.209                  from /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:19:
6.209 In function 'float32 b2Cross(const b2Vec2&, const b2Vec2&)',
6.209     inlined from 'bool b2ContactSolver::SolvePositionConstraints()' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:722:25:
6.209 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:396:32: warning: 'psm.b2PositionSolverManifold::normal.b2Vec2::x' may be used uninitialized [-Wmaybe-uninitialized]
6.209   396 |         return a.x * b.y - a.y * b.x;
6.209       |                            ~~~~^~~~~
6.210 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolvePositionConstraints()':
6.210 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:704:50: note: 'psm.b2PositionSolverManifold::normal.b2Vec2::x' was declared here
6.210   704 |                         b2PositionSolverManifold psm;
6.210       |                                                  ^~~
6.211 In function 'float32 b2Cross(const b2Vec2&, const b2Vec2&)',
6.211     inlined from 'bool b2ContactSolver::SolvePositionConstraints()' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:722:25:
6.211 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:396:36: warning: 'psm.b2PositionSolverManifold::normal.b2Vec2::y' may be used uninitialized [-Wmaybe-uninitialized]
6.211   396 |         return a.x * b.y - a.y * b.x;
6.211       |                                    ^
6.212 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolvePositionConstraints()':
6.212 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:704:50: note: 'psm.b2PositionSolverManifold::normal.b2Vec2::y' was declared here
6.212   704 |                         b2PositionSolverManifold psm;
6.212       |                                                  ^~~
6.212 In function 'b2Vec2 operator-(const b2Vec2&, const b2Vec2&)',
6.212     inlined from 'bool b2ContactSolver::SolvePositionConstraints()' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:712:24:
6.212 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:436:43: warning: 'psm.b2PositionSolverManifold::point.b2Vec2::x' may be used uninitialized [-Wmaybe-uninitialized]
6.212   436 |         return b2Vec2(a.x - b.x, a.y - b.y);
6.212       |                                           ^
6.215 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolvePositionConstraints()':
6.215 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:704:50: note: 'psm.b2PositionSolverManifold::point.b2Vec2::x' was declared here
6.215   704 |                         b2PositionSolverManifold psm;
6.215       |                                                  ^~~
6.216 In function 'b2Vec2 operator-(const b2Vec2&, const b2Vec2&)',
6.216     inlined from 'bool b2ContactSolver::SolvePositionConstraints()' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:712:24:
6.216 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:436:43: warning: 'psm.b2PositionSolverManifold::point.b2Vec2::y' may be used uninitialized [-Wmaybe-uninitialized]
6.216   436 |         return b2Vec2(a.x - b.x, a.y - b.y);
6.216       |                                           ^
6.216 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolvePositionConstraints()':
6.216 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:704:50: note: 'psm.b2PositionSolverManifold::point.b2Vec2::y' was declared here
6.216   704 |                         b2PositionSolverManifold psm;
6.216       |                                                  ^~~
6.217 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:704:50: warning: 'psm.b2PositionSolverManifold::separation' may be used uninitialized [-Wmaybe-uninitialized]
6.265 [ 54%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2PrismaticJoint.cpp.obj
6.282 In function 'float32 b2Cross(const b2Vec2&, const b2Vec2&)',
6.282     inlined from 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:813:25:
6.282 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:396:32: warning: 'psm.b2PositionSolverManifold::normal.b2Vec2::x' may be used uninitialized [-Wmaybe-uninitialized]
6.282   396 |         return a.x * b.y - a.y * b.x;
6.282       |                            ~~~~^~~~~
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)':
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:795:50: note: 'psm.b2PositionSolverManifold::normal.b2Vec2::x' was declared here
6.283   795 |                         b2PositionSolverManifold psm;
6.283       |                                                  ^~~
6.283 In function 'float32 b2Cross(const b2Vec2&, const b2Vec2&)',
6.283     inlined from 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:813:25:
6.283 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:396:36: warning: 'psm.b2PositionSolverManifold::normal.b2Vec2::y' may be used uninitialized [-Wmaybe-uninitialized]
6.283   396 |         return a.x * b.y - a.y * b.x;
6.283       |                                    ^
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)':
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:795:50: note: 'psm.b2PositionSolverManifold::normal.b2Vec2::y' was declared here
6.283   795 |                         b2PositionSolverManifold psm;
6.283       |                                                  ^~~
6.283 In function 'b2Vec2 operator-(const b2Vec2&, const b2Vec2&)',
6.283     inlined from 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:803:24:
6.283 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:436:43: warning: 'psm.b2PositionSolverManifold::point.b2Vec2::x' may be used uninitialized [-Wmaybe-uninitialized]
6.283   436 |         return b2Vec2(a.x - b.x, a.y - b.y);
6.283       |                                           ^
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)':
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:795:50: note: 'psm.b2PositionSolverManifold::point.b2Vec2::x' was declared here
6.283   795 |                         b2PositionSolverManifold psm;
6.283       |                                                  ^~~
6.283 In function 'b2Vec2 operator-(const b2Vec2&, const b2Vec2&)',
6.283     inlined from 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)' at /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:803:24:
6.283 /pinballnx/Box2D/include/Box2D/Common/b2Math.h:436:43: warning: 'psm.b2PositionSolverManifold::point.b2Vec2::y' may be used uninitialized [-Wmaybe-uninitialized]
6.283   436 |         return b2Vec2(a.x - b.x, a.y - b.y);
6.283       |                                           ^
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp: In member function 'bool b2ContactSolver::SolveTOIPositionConstraints(int32, int32)':
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:795:50: note: 'psm.b2PositionSolverManifold::point.b2Vec2::y' was declared here
6.283   795 |                         b2PositionSolverManifold psm;
6.283       |                                                  ^~~
6.283 /pinballnx/Box2D/Dynamics/Contacts/b2ContactSolver.cpp:795:50: warning: 'psm.b2PositionSolverManifold::separation' may be used uninitialized [-Wmaybe-uninitialized]
6.354 [ 54%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/gl_texture.cpp.obj
6.444 [ 55%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/gl_texture_buffer.cpp.obj
6.449 [ 56%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2PulleyJoint.cpp.obj
6.644 [ 57%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2RevoluteJoint.cpp.obj
6.660 [ 58%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/2xsal.cpp.obj
6.666 [ 58%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2RopeJoint.cpp.obj
6.723 [ 59%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2WeldJoint.cpp.obj
6.758 [ 59%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/bevel.cpp.obj
6.773 [ 60%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/Joints/b2WheelJoint.cpp.obj
6.837 [ 60%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2Body.cpp.obj
6.843 [ 61%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2ContactManager.cpp.obj
6.844 [ 62%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/color.cpp.obj
6.896 [ 63%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2Fixture.cpp.obj
7.085 [ 64%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_aperture.cpp.obj
7.140 [ 65%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2Island.cpp.obj
7.178 [ 66%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_caligari.cpp.obj
7.224 [ 66%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2World.cpp.obj
7.311 /pinballnx/Box2D/Dynamics/b2Body.cpp: In member function 'void b2Body::DestroyFixture(b2Fixture*)':
7.311 /pinballnx/Box2D/Dynamics/b2Body.cpp:232:14: warning: variable 'found' set but not used [-Wunused-but-set-variable]
7.311   232 |         bool found = false;
7.311       |              ^~~~~
7.323 [ 66%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_cgwg_fast.cpp.obj
7.372 [ 67%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Dynamics/b2WorldCallbacks.cpp.obj
7.435 [ 68%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_easymode.cpp.obj
7.474 [ 69%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_geom.cpp.obj
7.488 [ 70%] Building CXX object Box2D/CMakeFiles/Box2D.dir/Rope/b2Rope.cpp.obj
7.535 [ 70%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_pi.cpp.obj
7.542 [ 71%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_hyllian.cpp.obj
7.584 [ 72%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/crt_zfast.cpp.obj
7.588 [ 73%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/dot.cpp.obj
7.655 [ 73%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/lcd3x.cpp.obj
7.660 [ 74%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/retro_v2.cpp.obj
7.661 [ 75%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/scanlines.cpp.obj
7.663 [ 76%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/sabr_v3.cpp.obj
7.715 [ 76%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/sharp_bilinear.cpp.obj
7.715 [ 77%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/supereagle.cpp.obj
7.723 [ 78%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/sharp_bilinear_scanlines.cpp.obj
7.725 [ 78%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/texture.cpp.obj
7.788 [ 79%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/gl2/shaders/xbrz_freescale.cpp.obj
7.789 [ 79%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/switch/nxlink.cpp.obj
7.790 [ 80%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/posix/posix_clock.cpp.obj
7.797 [ 81%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/posix/posix_io.cpp.obj
7.801 [ 82%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/switch/switch_input.cpp.obj
7.845 [ 83%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/switch/switch_renderer.cpp.obj
7.871 [ 84%] Building CXX object libcross2d/CMakeFiles/cross2d.dir/source/platforms/switch/switch_sys.cpp.obj
8.451 [ 85%] Linking CXX static library libBox2D.a
8.533 [ 85%] Built target Box2D
9.057 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp: In member function 'virtual c2d::Input::Player* c2d::SWITCHInput::update(int)':
9.057 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:19:25: error: 'hidGetHandheldMode' was not declared in this scope
9.057    19 |     int handheld_mode = hidGetHandheldMode();
9.057       |                         ^~~~~~~~~~~~~~~~~~
9.095 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:26:65: error: 'HidControllerID' was not declared in this scope; did you mean 'FanController'?
9.095    26 |                     hidSetNpadJoyAssignmentModeSingleByDefault((HidControllerID) id);
9.095       |                                                                 ^~~~~~~~~~~~~~~
9.095       |                                                                 FanController
9.139 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:28:39: error: 'HidJoyHoldType_Horizontal' was not declared in this scope; did you mean 'HidNpadJoyHoldType_Horizontal'?     
9.139    28 |                 hidSetNpadJoyHoldType(HidJoyHoldType_Horizontal);
9.139       |                                       ^~~~~~~~~~~~~~~~~~~~~~~~~
9.139       |                                       HidNpadJoyHoldType_Horizontal
9.180 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:29:17: error: 'hidScanInput' was not declared in this scope
9.180    29 |                 hidScanInput();
9.180       |                 ^~~~~~~~~~~~
9.218 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:33:54: error: 'HidControllerID' was not declared in this scope; did you mean 'FanController'?
9.218    33 |                     hidSetNpadJoyAssignmentModeDual((HidControllerID) id);
9.218       |                                                      ^~~~~~~~~~~~~~~
9.218       |                                                      FanController
9.263 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:37:47: error: 'HidControllerID' was not declared in this scope; did you mean 'FanController'?
9.263    37 |                     if (hidGetControllerType((HidControllerID) id0) & TYPE_JOYCON_LEFT) {
9.263       |                                               ^~~~~~~~~~~~~~~
9.263       |                                               FanController
9.301 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:37:25: error: 'hidGetControllerType' was not declared in this scope; did you mean 'SetSysControllerType'?
9.301    37 |                     if (hidGetControllerType((HidControllerID) id0) & TYPE_JOYCON_LEFT) {
9.301       |                         ^~~~~~~~~~~~~~~~~~~~
9.301       |                         SetSysControllerType
9.343 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:37:71: error: 'TYPE_JOYCON_LEFT' was not declared in this scope
9.343    37 |                     if (hidGetControllerType((HidControllerID) id0) & TYPE_JOYCON_LEFT) {
9.343       |                                                                       ^~~~~~~~~~~~~~~~
9.344 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:39:71: error: expected ')' before 'id1'
9.344    39 |                             if (hidGetControllerType((HidControllerID) id1) & TYPE_JOYCON_RIGHT) {
9.344       |                                                     ~                 ^~~~
9.344       |                                                                       )
9.395 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:39:79: error: 'TYPE_JOYCON_RIGHT' was not declared in this scope
9.395    39 |                             if (hidGetControllerType((HidControllerID) id1) & TYPE_JOYCON_RIGHT) {
9.395       |                                                                               ^~~~~~~~~~~~~~~~~
9.395 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:43:81: error: expected ')' before 'id0'
9.395    43 |                                     hidMergeSingleJoyAsDualJoy((HidControllerID) id0, (HidControllerID) id1);
9.395       |                                                               ~                 ^~~~
9.395       |                                                                                 )
9.395 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:43:104: error: expected ')' before 'id1'
9.395    43 |                                     hidMergeSingleJoyAsDualJoy((HidControllerID) id0, (HidControllerID) id1);
9.395       |                                                               ~                                        ^~~~
9.395       |                                                                                                        )
9.395 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:45:81: error: expected ')' before 'id1'
9.395    45 |                                     hidMergeSingleJoyAsDualJoy((HidControllerID) id1, (HidControllerID) id0);
9.395       |                                                               ~                 ^~~~
9.395       |                                                                                 )
9.395 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:45:104: error: expected ')' before 'id0'
9.395    45 |                                     hidMergeSingleJoyAsDualJoy((HidControllerID) id1, (HidControllerID) id0);
9.395       |                                                               ~                                        ^~~~
9.395       |                                                                                                        )
9.443 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:61:43: error: 'HidControllerID' was not declared in this scope; did you mean 'FanController'?
9.443    61 |                 if (hidGetControllerType((HidControllerID) index) & TYPE_JOYCON_LEFT) {
9.443       |                                           ^~~~~~~~~~~~~~~
9.443       |                                           FanController
9.501 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:61:21: error: 'hidGetControllerType' was not declared in this scope; did you mean 'SetSysControllerType'?
9.501    61 |                 if (hidGetControllerType((HidControllerID) index) & TYPE_JOYCON_LEFT) {
9.501       |                     ^~~~~~~~~~~~~~~~~~~~
9.501       |                     SetSysControllerType
9.553 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:61:69: error: 'TYPE_JOYCON_LEFT' was not declared in this scope
9.553    61 |                 if (hidGetControllerType((HidControllerID) index) & TYPE_JOYCON_LEFT) {
9.553       |                                                                     ^~~~~~~~~~~~~~~~
9.553 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:63:66: error: expected ')' before 'index'
9.553    63 |                 } else if (hidGetControllerType((HidControllerID) index) & TYPE_JOYCON_RIGHT) {
9.553       |                                                ~                 ^~~~~~
9.553       |                                                                  )
9.606 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:63:76: error: 'TYPE_JOYCON_RIGHT' was not declared in this scope
9.606    63 |                 } else if (hidGetControllerType((HidControllerID) index) & TYPE_JOYCON_RIGHT) {
9.606       |                                                                            ^~~~~~~~~~~~~~~~~
9.606 /pinballnx/libcross2d/source/platforms/switch/switch_input.cpp:60:21: warning: unused variable 'index' [-Wunused-variable]
9.606    60 |                 int index = (int) SDL_JoystickInstanceID(joystick);
9.606       |                     ^~~~~
9.728 make[3]: *** [libcross2d/CMakeFiles/cross2d.dir/build.make:1003: libcross2d/CMakeFiles/cross2d.dir/source/platforms/switch/switch_input.cpp.obj] Error 1
9.728 make[3]: *** Waiting for unfinished jobs....
12.31 In file included from /pinballnx/libcross2d/source/platforms/gl2/gl_texture.cpp:12:
12.31 /pinballnx/libcross2d/include/cross2d/skeleton/stb_image.h: In function 'int stbi__parse_png_file(stbi__png*, int, int)':
12.31 /pinballnx/libcross2d/include/cross2d/skeleton/stb_image.h:4882:62: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
12.31  4882 |                         for (k = 0; k < s->img_n; ++k) tc[k] = (stbi_uc)(stbi__get16be(s) & 255) * stbi__depth_scale_table[z->depth]; // non 8-bit images will be larger
12.31       |                                                        ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
12.31 /pinballnx/libcross2d/include/cross2d/skeleton/stb_image.h:4801:26: note: at offset 3 into destination object 'tc' of size 3
12.31  4801 |     stbi_uc has_trans=0, tc[3]={0};
12.31       |                          ^~
14.98 make[2]: *** [CMakeFiles/Makefile2:161: libcross2d/CMakeFiles/cross2d.dir/all] Error 2
14.98 make[1]: *** [CMakeFiles/Makefile2:430: games/pinball/CMakeFiles/pinball.nro.dir/rule] Error 2
14.98 make: *** [Makefile:273: pinball.nro] Error 2
------
dockerfile:23
--------------------
  22 |
  23 | >>> RUN mkdir cmake-build && cd cmake-build && \
  24 | >>>     cmake -DPLATFORM_SWITCH=ON -DCMAKE_BUILD_TYPE=Release ../ && \
  25 | >>>     make pinball.nro -j$(nproc)
  26 |     
--------------------
ERROR: failed to build: failed to solve: process "/bin/sh -c mkdir cmake-build && cd cmake-build &&     cmake -DPLATFORM_SWITCH=ON -DCMAKE_BUILD_TYPE=Release ../ &&     make pinball.nro -j$(nproc)" did not complete successfully: exit code: 2```
